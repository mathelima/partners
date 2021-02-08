#cnpj, description, partnership_status
import pytest

from src.models.partner import Partner

@pytest.mark.parametrize("cnpj", [.32, 10, True])
def test_cnpj_type(cnpj):
    with pytest.raises(TypeError):
        partner = Partner(cnpj, "valid description", "not initiated")
        print(partner.name)


@pytest.mark.parametrize("cnpj", ["", "dasdf"])
def test_cnpj_value(cnpj):
    with pytest.raises(ValueError):
        partner = Partner(cnpj, "valid description", "not initiated")


@pytest.mark.parametrize("description", [.32, 10, True])
def test_description_type(description):
    with pytest.raises(TypeError):
        partner = Partner("18552346000168", description, "not initiated")

@pytest.mark.parametrize("description", ["a"*300," " ])
def test_description_value(description):
    with pytest.raises(ValueError):
        partner = Partner("18552346000168", description, "not initiated")


@pytest.mark.parametrize("partnership_status", [.32, 10, True])
def test_partnership_status_type(partnership_status):
    with pytest.raises(TypeError):
        partner = Partner("18552346000168", "valid description", partnership_status)

@pytest.mark.parametrize("partnership_status", ["a"*300, " "])
def test_partnership_status_value(partnership_status):
    with pytest.raises(ValueError):
        partner = Partner("18552346000168", "valid description", partnership_status)
