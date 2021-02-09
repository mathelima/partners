import sys

sys.path.append('.')

import pytest
from src.models.partner import Partner
from src.dao.partner_dao import PartnerDao
from sqlalchemy.orm.exc import UnmappedInstanceError


class TestPartnerDao:
    dao = PartnerDao()

    @pytest.fixture
    def create_instance(self):
        partner = Partner("18552346000168", "Olist Description", "not initiated")
        return partner

    def test_instance(self):
        assert isinstance(self.dao, PartnerDao)

    def test_save(self, create_instance):
        partner_saved = self.dao.save(create_instance)
        assert partner_saved.id_ is not None
        self.dao.delete(partner_saved)

    def test_read_by_id(self, create_instance):
        partner_saved = self.dao.save(create_instance)
        partner_read = self.dao.read_by_id(partner_saved.id_)
        assert isinstance(partner_read, Partner)
        self.dao.delete(partner_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            self.dao.read_by_id('id')

    def test_read_all(self):
        result = self.dao.read_all()
        assert isinstance(result, list)

    def test_delete(self, create_instance):
        partner_saved = self.dao.save(create_instance)
        partner_read = self.dao.read_by_id(partner_saved.id_)
        self.dao.delete(partner_read)
        partner_read = self.dao.read_by_id(partner_saved.id_)
        assert partner_read is None

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.save('String')

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            self.dao.delete('String')
