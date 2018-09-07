
import pytest
from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def test_get_orders(client):
    response = client.get('/api/v1/orders')
    assert response.status_code == 200

def test_orders_post(client):
    response = client.post('api/v1/orders?item=Burger&quantity=2')
    assert response.status_code == 201

def test_update_orders(client):
    response = client.put('api/v1/orders/1?status=accepted')
    assert response.status_code == 201