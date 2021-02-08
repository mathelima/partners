import re
import requests
from datetime import datetime
import time
import json

from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from src.models.base_model import BaseModel

Base = declarative_base()

class Partner(BaseModel):
    __tablename__ = "PARTNER"
    id_ = Column(Integer, primary_key=True)
    cnpj = Column(String(length=50))
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    partnership_status = Column(String(length=20), default="Not Initiated")
    uf = Column(String(length=2))
    phone = Column(String(length=20))
    email = Column(String(length=50))
    cnpj_status = Column(String(length=50))

    def __init__(self, cnpj, description, partnership_status):

        self.description = description
        self.partnership_status = partnership_status

        rqst = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
        result = json.loads(rqst.content)

        self.cnpj = cnpj
        self.name = result["nome"]
        self.uf = result["uf"]
        self.phone = result["telefone"]
        self.email = result["email"]
        self.cnpj_status = result["situacao"]
        time.sleep(3)

    def transform_string(self, string):
        string = string.capitalize()
        string = re.sub(r"\s+", " ", string)
        string = string.strip()
        return string

    @validates("cnpj")
    def validate_cnpj(self, key, cnpj):
        if not isinstance(cnpj, str):
            raise TypeError("CNPJ must be str.")
        if not re.search(r"\d", cnpj):
            raise ValueError("There must be numbers in CNPJ.")
        
        cnpj = "".join(re.findall(r"\d", cnpj))
        return cnpj

    @validates("name")
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name type must be str.")
        if len(name) > 50:
            raise ValueError("Name length must not exceed 50 characters.")
        if not name.strip():
            raise ValueError("Name must not be empty.")
        
        name = self.transform_string(name)
        return name

    @validates("uf")
    def validate_name(self, key, uf):
        if not isinstance(uf, str):
            raise TypeError("UF must be str.")
        return uf

    @validates("email")
    def validate_name(self, key, email):
        if not isinstance(email, str):
            raise TypeError("E-mail must be str.")
        return email
    
    @validates("phone")
    def validate_name(self, key, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be str.")
        return phone
    
    @validates("cnpj_status")
    def validate_name(self, key, cnpj_status):
        if not isinstance(cnpj_status, str):
           raise TypeError("CPJ STATUS must be str.")
        return cnpj_status

    @validates("description")
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description type must be str.")
        if len(description) > 200:
            raise ValueError("Description length must not exceed 50 characters.")
        if not description.strip():
            raise ValueError("Description must not be empty.")
        
        description = self.transform_string(description)
        return description

    @validates("created_at")
    def validate_created_at(self, key, created_at):
        if not isinstance(created_at, datetime.datetime):
            raise TypeError("Datetime must be datetime.")

    @validates("partnership_status")
    def validate_partnership_status(self, key, partnership_status):
        if not isinstance(partnership_status, str):
            raise TypeError("Partnership_status type must be str.")
        if len(partnership_status) > 20:
            raise ValueError("Partnership_status length must not exceed 20 characters.")
        if not partnership_status.strip():
            raise ValueError("Partnership_status must not be empty.")
        
        partnership_status = partnership_status.lower()
        if partnership_status not in ["not initiated", "ongoing", "done"]:
            raise ValueError("Partnership Status must be one of ['not initiated', 'ongoing', 'done']")
        return partnership_status