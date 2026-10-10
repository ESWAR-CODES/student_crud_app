from sqlalchemy.orm import Session
from app import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    """Creates a new student record in the database."""
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    """Retrieves a list of students with optional pagination (filtering)."""
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    """Retrieves a single student by their unique ID."""
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def update_student(db: Session, student_id: int, student_data: schemas.StudentUpdate):
    """Updates an existing student's details."""
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if db_student:
        update_data = student_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_student, key, value)
        
        db.commit()
        db.refresh(db_student)
        
    return db_student

def delete_student(db: Session, student_id: int):
    """Deletes a student record from the database."""
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if db_student:
        db.delete(db_student)
        db.commit()
        
    return db_student