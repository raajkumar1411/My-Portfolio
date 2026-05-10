import json
import os
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mohan Kumar Portfolio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve Portfolio HTML assets (thumbnails, profile images, etc.)
portfolio_html_dir = os.path.join(os.path.dirname(__file__), "..", "Portfolio HTML")
if os.path.isdir(portfolio_html_dir):
    app.mount("/assets", StaticFiles(directory=portfolio_html_dir), name="assets")


@app.get("/health")
def health():
    return {"status": "ok", "message": "Portfolio API is running"}


@app.get("/api/profile", response_model=schemas.ProfileOut)
def get_profile(db: Session = Depends(get_db)):
    profile = db.query(models.Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found — run seed.py first")
    return profile


@app.get("/api/portfolio", response_model=List[schemas.PortfolioItemOut])
def get_portfolio(category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.PortfolioItem)
    if category:
        query = query.filter(models.PortfolioItem.category == category)
    return query.order_by(models.PortfolioItem.sort_order).all()


@app.get("/api/services", response_model=List[schemas.ServiceOut])
def get_services(db: Session = Depends(get_db)):
    rows = db.query(models.Service).order_by(models.Service.sort_order).all()
    result = []
    for s in rows:
        result.append(schemas.ServiceOut(
            id=s.id,
            icon=s.icon,
            title=s.title,
            description=s.description,
            items=json.loads(s.items_json),
            sort_order=s.sort_order,
        ))
    return result


@app.get("/api/skills", response_model=List[schemas.SkillOut])
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).order_by(models.Skill.sort_order).all()


@app.get("/api/testimonials", response_model=List[schemas.TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return db.query(models.Testimonial).order_by(models.Testimonial.sort_order).all()


@app.post("/api/contact", response_model=schemas.ContactMessageOut)
def submit_contact(msg: schemas.ContactMessageIn, db: Session = Depends(get_db)):
    if not msg.name.strip() or not msg.email.strip() or not msg.message.strip():
        raise HTTPException(status_code=422, detail="Name, email, and message are required")
    db_msg = models.ContactMessage(
        name=msg.name.strip(),
        email=msg.email.strip(),
        project_type=msg.project_type,
        message=msg.message.strip(),
    )
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg


@app.get("/api/messages", response_model=List[schemas.ContactMessageOut])
def get_messages(db: Session = Depends(get_db)):
    return db.query(models.ContactMessage).order_by(models.ContactMessage.created_at.desc()).all()
