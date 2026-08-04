from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Student
from schemas import StudentCreate

from schemas import UserCreate
from models import User
from utils import hash_password

from fastapi.security import OAuth2PasswordRequestForm

from utils import verify_password

from auth import create_access_token



from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5176",
        "http://127.0.0.1:5176",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from auth import verify_token

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_token(token)

    if payload is None:
        return {"message": "Invalid Token"}

    return payload


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        name=student.name,
        age=student.age,
        department=student.department
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get("/students")
def get_students(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Student).all()

@app.get("/students/{id}")
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return {"message": "Student not found"}

    return student

@app.put("/students/{id}")
def update_student(id: int, student: StudentCreate, db: Session = Depends(get_db)):

    data = db.query(Student).filter(Student.id == id).first()

    if not data:
        return {"message": "Student not found"}

    data.name = student.name
    data.age = student.age
    data.department = student.department

    db.commit()
    db.refresh(data)

    return data

@app.delete("/students/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):

    data = db.query(Student).filter(Student.id == id).first()

    if not data:
        return {"message": "Student not found"}

    db.delete(data)
    db.commit()

    return {"message": "Student deleted successfully"}

from fastapi import HTTPException

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()

        if existing_user:
            return {"message": "Email already exists"}

        hashed = hash_password(user.password)

        new_user = User(
            username=user.username,
            email=user.email,
            password=hashed
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User Registered Successfully"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:
        return {"message": "Invalid Email"}

    if not verify_password(
        form_data.password,
        user.password
    ):
        return {"message": "Wrong Password"}

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    

