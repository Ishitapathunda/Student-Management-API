from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    department: str

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student Added", "student": student}

@app.get("/students")
def get_students():
    return students

@app.put("/students/{id}")
def update_student(id: int, student: Student):
    if id >= len(students):
        return {"error": "Student not found"}

    students[id] = student
    return {"message": "Student Updated", "student": student}

@app.delete("/students/{id}")
def delete_student(id: int):
    if id >= len(students):
        return {"error": "Student not found"}

    deleted = students.pop(id)
    return {"message": "Student Deleted", "student": deleted}