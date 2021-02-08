from src.dao.base_dao import BaseDao
from src.models.partner import Partner


class PartnerDao(BaseDao):
    def __init__(self):
        super().__init__(Partner)