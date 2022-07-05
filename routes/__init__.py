# Funciones externas
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

# Funciones locales
from models import Base, Sample
from config import engine, SessionLocal
from schemas import Sample as sample, message

# Inicializar modelos
Base.metadata.create_all(bind=engine)

# Inicializar rutas
route = APIRouter()


def get_db():
    # Obtener estado de la conexion
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.get("/getSamples", response_model=List[sample])
# Obtener lista de registros
#
# Metodo: GET
# Headers: None
# Req: None
# Response:
#   [
#       {
#           "first_name": string,
#           "last_name": string,
#           "company_name": string,
#           "address": string,
#           "state": string,
#           "zip": string,
#           "phone1": string,
#           "phone2": string,
#           "email": string,
#           "department": string,
#           "city": string,
#       }
#   ]
def getSamples(db: Session = Depends(get_db)):
    return db.query(Sample).all()


@route.get("/getSample", response_model=sample)
# Obtener registro unico
#
# Metodo: GET
# Headers: None
# Req:
# {
#   "first_name": string,
#   "last_name": string,
#   "department": string
# }
# Response:
#   {
#       "first_name": string,
#       "last_name": string,
#       "company_name": string,
#       "address": string,
#       "state": string,
#       "zip": string,
#       "phone1": string,
#       "phone2": string,
#       "email": string,
#       "department": string,
#       "city": string,
#   }
def getSample(first_name: str, last_name: str, department: str, db: Session = Depends(get_db)):
    return db.query(Sample).filter(
        (Sample.first_name == first_name),
        (Sample.last_name == last_name),
        (Sample.department == department)).first()


@route.post("/createSample", response_model=message)
# Crear registro
#
# Metodo: POST
# Headers: None
# Req:
# {
#   "first_name": string,
#   "last_name": string,
#   "company_name": string,
#   "address": string,
#   "state": string,
#   "zip": string,
#   "phone1": string,
#   "phone2": string,
#   "email": string,
#   "department": string,
#   "city": string,
# }
# Response:
# {
#   message: string
# }
def createSample(item: sample, db: Session = Depends(get_db)):
    response_message = message(message='false')

    try:
        sample_new = Sample(
            first_name=item.first_name,
            last_name=item.last_name,
            company_name=item.company_name,
            address=item.address,
            city=item.city,
            state=item.state,
            zip=item.zip,
            phone1=item.phone1,
            phone2=item.phone2,
            email=item.email,
            department=item.department
        )

        db.add(sample_new)
        db.commit()

        response_message.message = 'true'

        return response_message
    except (IntegrityError, ValueError) as ex:
        # print(ex)

        return response_message


@route.put('/updateSample', response_model=message)
# Actualizar registro
#
# Metodo: PUT
# Headers: None
# Req:
# {
#   "first_name": string,
#   "last_name": string,
#   "company_name": string,
#   "address": string,
#   "state": string,
#   "zip": string,
#   "phone1": string,
#   "phone2": string,
#   "email": string,
#   "department": string,
#   "city": string,
# }
# Response:
# {
#   message: string
# }
def updateSample(item: sample, db: Session = Depends(get_db)):
    response_message = message(message='false')

    try:

        sample_update = db.query(Sample).filter(
            (Sample.first_name == item.first_name),
            (Sample.last_name == item.last_name),
            (Sample.department == item.department)).first()

        if sample_update == None:
            return response_message

        sample_update.company_name = item.company_name
        sample_update.address = item.address
        sample_update.city = item.city
        sample_update.state = item.state
        sample_update.zip = item.zip
        sample_update.phone1 = item.phone1
        sample_update.phone2 = item.phone2
        sample_update.email = item.email

        db.commit()

        response_message.message = 'true'

        return response_message
    except (IntegrityError, ValueError) as ex:
        # print(ex)

        return response_message


@route.delete('/deleteSample', response_model=message)
# Borrar registro
#
# Metodo: delete
# Headers: None
# Req:
# {
#   "first_name": string,
#   "last_name": string,
#   "department": string
# }
# Response:
# {
#   message: string
# }
def deleteSample(first_name: str, last_name: str, department: str, db: Session = Depends(get_db)):
    response_message = message(message='false')

    try:

        sample_delete = db.query(Sample).filter(
            (Sample.first_name == first_name),
            (Sample.last_name == last_name),
            (Sample.department == department)).first()

        if sample_delete == None:
            return response_message

        db.delete(sample_delete)
        db.commit()

        response_message.message = 'true'

        return response_message
    except (IntegrityError, ValueError) as ex:
        # print(ex)

        return response_message
