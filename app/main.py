from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, crud, ai
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EWB Student CRUD API",
    description="Backend API for managing student records.",
    version="1.0.0"
)
from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def root():
    """Redirects the root URL to the API documentation."""
    return RedirectResponse(url="/docs")

@app.post("/students", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    """Create a new student record."""
    # Check if email already exists to prevent duplicate entries
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_student(db=db, student=student)

@app.get("/students", response_model=List[schemas.StudentResponse])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List or filter all students."""
    return crud.get_students(db, skip=skip, limit=limit)

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    """View a single student by ID."""
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student_data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    """Update details of an existing student."""
    db_student = crud.update_student(db, student_id=student_id, student_data=student_data)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete a student record."""
    db_student = crud.delete_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return None

@app.post("/ask-ai", tags=["AI Extension"])
def ask_ai(query: schemas.AIQuery, db: Session = Depends(get_db)):
    """Ask natural language questions about the student database."""
    try:
        # Fetch an accurate, human-readable response grounded in database records
        answer = ai.ask_ollama_about_students(db, query.question)
        return {"question": query.question, "answer": answer}
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"AI Error: Ensure Ollama is running locally. Details: {str(e)}"
        )