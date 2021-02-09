from src.resources.base_resource import BaseResource
from flask_restful import fields, marshal_with
from src.dao.partner_dao import PartnerDao
from src.models.partner import Partner


class PartnerResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "cnpj": fields.String,
        "name": fields.String,
        "description": fields.String,
        "created_at": fields.String,
        "partnership_status": fields.String,
        "uf": fields.String,
        "phone": fields.String,
        "email": fields.String,
        "cnpj_status": fields.String
    }

    def __init__(self):
        self.__dao = PartnerDao()
        self.__model_type = Partner
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
