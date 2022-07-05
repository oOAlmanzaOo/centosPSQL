from sqlalchemy import Column, CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy.sql.sqltypes import String

from config import Base


class Sample(Base):
    # Nombre de la tabla
    __tablename__ = "samples"

    # Especificacion de columnas
    first_name = Column(String(50), primary_key=True)
    last_name = Column(String(50), primary_key=True)
    company_name = Column(String(50))
    address = Column(String(50))
    city = Column(String(50))
    state = Column(String(2), CheckConstraint(
        'char_length(state) > 0 AND char_length(state) < 3 AND state ~ \'[A-Za-z]{2}\''))
    zip = Column(String(50))
    phone1 = Column(String(50))
    phone2 = Column(String(50))
    email = Column(String(50))
    department = Column(String(50), primary_key=True)

    @validates('state')
    def validate_code(self, key, field):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if field and len(field) > max_len:
            raise ValueError("state invalid")
            # return field[:max_len]
        return field
