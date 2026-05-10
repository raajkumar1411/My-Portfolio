from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    tagline = Column(Text)
    location = Column(String)
    email = Column(String)
    phone = Column(String)
    whatsapp_url = Column(String)
    instagram_url = Column(String)
    youtube_url = Column(String)
    linkedin_url = Column(String)
    facebook_url = Column(String)
    profile_image = Column(String)
    years_experience = Column(String)
    projects_done = Column(String)
    happy_clients = Column(String)
    platforms_mastered = Column(String)
    about_text_1 = Column(Text)
    about_text_2 = Column(Text)


class PortfolioItem(Base):
    __tablename__ = "portfolio_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String, index=True)
    category_label = Column(String)
    description = Column(Text)
    drive_id = Column(String, nullable=True)
    thumbnail_url = Column(String, nullable=True)
    sort_order = Column(Integer, default=0)


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    icon = Column(String)
    title = Column(String)
    description = Column(Text)
    items_json = Column(Text)
    sort_order = Column(Integer, default=0)


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    icon_text = Column(String)
    icon_class = Column(String)
    name = Column(String)
    percentage = Column(Integer)
    description = Column(String)
    sort_order = Column(Integer, default=0)


class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    client_role = Column(String)
    text = Column(Text)
    stars = Column(Integer, default=5)
    sort_order = Column(Integer, default=0)


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    project_type = Column(String)
    message = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
