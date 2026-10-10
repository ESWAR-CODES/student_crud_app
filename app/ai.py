import ollama
from sqlalchemy.orm import Session
from app import crud

def ask_ollama_about_students(db: Session, question: str) -> str:
    """Fetches database records and passes them to Ollama as context."""
    students = crud.get_students(db, skip=0, limit=100)
    
    if not students:
        context = "No students currently in the database."
    else:
        context = "Student Records:\n"
        for s in students:
            context += f"- ID: {s.id}, Name: {s.name}, DOB: {s.date_of_birth}, Email: {s.email}, Course: {s.course}\n"

    prompt = f"""
    You are an AI assistant for a student database. Use ONLY the following context to answer the user's question. 
    Keep the answer concise and accurate.
    
    Context:
    {context}
    
    Question: {question}
    """
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'system', 'content': 'You are a helpful and secure database assistant.'},
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']