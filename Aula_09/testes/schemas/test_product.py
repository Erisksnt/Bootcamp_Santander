from testes.factories import product_data
from store.schemas.product import ProductIn
from uuid import UUID


def test_schemas_returns_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID)


def test_schemas_returns_raise():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID)
