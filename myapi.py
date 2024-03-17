from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name': 'John',
        'age': 17,
        'year': 'X'
    },
    2: {
        'name': 'David',
        'age': 19,
        'year': 'XII'
    },
    3: {
        'name': 'Michael',
        'age': 21,
        'year': 'XI'
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get('/')
def index():
    return {"Name": "First Data"}

@app.get('/get-student/{student_id}')
def get_student(student_id: int):
    return students[student_id]

@app.get('/get-all-students')
def get_all_student():
    return students

@app.get('/get-by-name/{student_id}')
def get_student(student_id: int, name: str = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return "Data not found"

@app.post('/create_student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return "Error: Student Exists"
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return 'No Student Found'
    
    if student.name != 'string':
        students[student_id].name = student.name
    if student.age != 0:
        students[student_id].age = student.age
    if student.year != 'string':
        students[student_id].year = student.year

    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return 'No Student Found'
    del students[student_id]
    return f'Deleted {student_id}'