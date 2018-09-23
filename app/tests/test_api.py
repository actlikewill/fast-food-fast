
import pytest
from flask import json
from app import create_app

json_orders = [
    {    
	"item":"Burger",
	"quantity":"2",
	"status":"Pending"    
    },
    {
	"item":"Chicken",
	"quantity":"3",
	"status":"Pending"
    },
    {	
	"status":"accepted"
    }
    ]


@pytest.fixture
def client(request):
    test_client = create_app('default').test_client()
    return test_client

def test_get_orders(client):
    response = client.get('/api/v1/orders')
    assert response.status_code == 200

def test_orders_post_burger(client):
    response = client.post('/api/v1/orders', data=json.dumps(json_orders[0]),
                             content_type='application/json')
    assert response.status_code == 201
    assert b'Burger' in response.data

def test_orders_post_chicken(client):
    response = client.post('/api/v1/orders', data=json.dumps(json_orders[1]),
                             content_type='application/json')
    assert response.status_code == 201
    assert b'Chicken' in response.data

def test_update_orders(client):
    response = client.put('/api/v1/orders/1', data=json.dumps(json_orders[2]),
                             content_type='application/json')
    assert b'accepted' in response.data
    assert response.status_code == 201

def test_get_single_order(client):
    response = client.get('/api/v1/orders/1')
    assert response.status_code == 200

def test_error_no_order(client):
    response = client.get('/api/v1/orders/3')
    assert b'error' in response.data
    assert response.status_code == 404
    