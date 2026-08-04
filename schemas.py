from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    age: int
    department: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str