
import pytest
from app import create_app

@pytest.fixture
def client(request):
    test_client = create_app('default').test_client()    
    return test_client

def test_get_orders(client):
    response = client.get('/api/v1/orders')
    assert response.status_code == 200

def test_orders_post(client):
    response = client.post('/api/v1/orders?item=Burger&quantity=2')
    assert response.status_code == 201
    assert b'Burger' in response.data

def test_update_orders(client):
    response = client.put('/api/v1/orders/1?status=accepted')
    assert b'accepted' in response.data 
    assert response.status_code == 201

def test_error_404(client):
    response = client.get('/api/v1/orders/1')
    assert response.status_code == 200

def test_error_no_order(client):
    response = client.get('/api/v1/orders/2')
    assert b'error' in response.data
    assert response.status_code == 404

def test_no_quantity(client):
    response = client.post('/api/v1/orders?item=Burger')
    assert b'sorry' in response.data

def test_no_item(client):
    response = client.post('/api/v1/orders?quantity=1')
    assert b'sorry' in response.data