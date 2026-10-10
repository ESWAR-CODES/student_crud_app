from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Student(Base):
    """
    SQLAlchemy model representing the students table in SQLite.
    Includes all mandatory and optional fields from the project specifications.
    """
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=False)

    course = Column(String(100), nullable=True)
    address = Column(String(255), nullable=True)
    enrollment_date = Column(Date, nullable=True)