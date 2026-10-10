# EWB Student Database CRUD Application

An individual backend development project built for the EWB Edu Tech Pvt. Ltd. Internship Assignment. This application provides a RESTful API to manage student records using full Create, Read, Update, and Delete (CRUD) operations, backed by persistent SQLite storage. 

Additionally, it features an **Optional AI Extension** using a local Ollama model to answer natural-language queries about the database securely.

## 🚀 Technologies Used
* **Framework:** FastAPI
* **Database:** SQLite & SQLAlchemy (ORM)
* **Data Validation:** Pydantic
* **Local AI:** Ollama (`llama3.2:1b`)
* **Server:** Uvicorn

---

## 📋 Prerequisites
Before running this project, ensure you have the following installed:
* Python 3.9+
* Git
* [Ollama](https://ollama.com/) (Required only if testing the AI extension)

---

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ESWAR-CODES/student_crud_app.git](https://github.com/ESWAR-CODES/student_crud_app.git)
cd student_crud_app

2. Create and activate a virtual environment:

Bash
# On Windows (CMD/PowerShell)
python -m venv venv
venv\Scripts\activate
3. Install dependencies:

Bash
pip install -r requirements.txt
4. Pull the AI Model (Optional):
To use the natural-language querying feature, download the specific Llama model:

Bash
ollama run llama3.2:1b
(Type /bye to exit the prompt once it finishes downloading).

💻 Run Commands
Start the local Uvicorn development server:

Bash
uvicorn app.main:app --reload
The server will start at http://127.0.0.1:8000.

🧪 API Testing Instructions
FastAPI provides an automatic, interactive testing interface.

Run the server using the command above.

Open your web browser and navigate to: http://127.0.0.1:8000/docs

Sample Requests to Test in Swagger UI:
POST /students: Create a new student by providing a JSON body with name, date_of_birth (YYYY-MM-DD), email, and phone. (Testing missing-record validation: duplicate emails will return a 400 Error).

GET /students: Retrieves a list of all saved students.

GET /students/{student_id}: View a specific student's profile. (Testing missing-record validation: invalid IDs return a 404 Error).

PUT /students/{student_id}: Partially update an existing student (e.g., add an optional course or address).

DELETE /students/{student_id}: Remove a student from the database.

POST /ask-ai: Submit a question like "How many students are there?" to see the AI interpret the SQLite data.

🔒 Security Note
This repository uses dummy data for demonstration purposes. No real student personal information, passwords, or secrets have been committed. The AI integration strictly uses text context and does not execute raw SQL queries.