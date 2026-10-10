from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    """Shared student attributes across schemas."""
    name: str
    date_of_birth: date
    email: str
    phone: str
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None


class StudentCreate(StudentBase):
    """Schema for incoming requests when creating a new student."""
    pass


class StudentUpdate(BaseModel):
    """Schema for updating an existing student (all fields optional)."""
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None


class StudentResponse(StudentBase):
    """Schema for student responses returned from the API."""
    id: int

    model_config = ConfigDict(from_attributes=True)


class AIQuery(BaseModel):
    """Schema for AI natural language queries."""
    question: str