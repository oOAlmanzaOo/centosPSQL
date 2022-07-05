# Funciones externas
from pydantic import BaseModel


class Sample(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    address: str
    state: str
    zip: str
    phone1: str
    phone2: str
    email: str
    department: str
    city: str

    class Config:
        orm_mode = True

class message(BaseModel):
    message: str

    class Config:
        orm_mode = True