from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ProfileOut(BaseModel):
    id: int
    name: str
    title: str
    tagline: str
    location: str
    email: str
    phone: str
    whatsapp_url: str
    instagram_url: str
    youtube_url: str
    linkedin_url: str
    facebook_url: str
    profile_image: str
    years_experience: str
    projects_done: str
    happy_clients: str
    platforms_mastered: str
    about_text_1: str
    about_text_2: str

    model_config = {"from_attributes": True}


class PortfolioItemOut(BaseModel):
    id: int
    title: str
    category: str
    category_label: str
    description: str
    drive_id: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: int

    model_config = {"from_attributes": True}


class ServiceOut(BaseModel):
    id: int
    icon: str
    title: str
    description: str
    items: List[str]
    sort_order: int


class SkillOut(BaseModel):
    id: int
    icon_text: str
    icon_class: str
    name: str
    percentage: int
    description: str
    sort_order: int

    model_config = {"from_attributes": True}


class TestimonialOut(BaseModel):
    id: int
    client_name: str
    client_role: str
    text: str
    stars: int
    sort_order: int

    model_config = {"from_attributes": True}


class ContactMessageIn(BaseModel):
    name: str
    email: str
    project_type: str
    message: str


class ContactMessageOut(BaseModel):
    id: int
    name: str
    email: str
    project_type: str
    message: str
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
