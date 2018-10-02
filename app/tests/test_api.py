
import pytest
from flask import json
from app import create_app

json_data = [
    {
	"Burger":2
    },
    {
	"Chicken":4
    },
    {
	"status":"accepted"
    },
    {
    "menu_item":"Burger",
    "price": 250
    },
    {
    "menu_item":"Ice Cream",
    "price": 400
    },
    {
    "Sandwich": 5
    },
    {
    "menu_item":"Burg3r",
    "price": 250
    }
    ]


@pytest.fixture
def client(request):
    test_client = create_app('default').test_client()
    return test_client

def test_update_menu_item_no_menu(client):
    response = client.put('/api/v1/menu/1', data=json.dumps(json_data[4]),
                             content_type='application/json')
    assert b'item does not exist' in response.data
    assert response.status_code == 404

def test_add_menu_item(client):
    response = client.post('/api/v1/menu', data=json.dumps(json_data[3]),
                             content_type='application/json')
    assert b'Burger' in response.data
    assert response.status_code == 201

def test_add_menu_invalid_item(client):
    response = client.post('/api/v1/menu', data=json.dumps(json_data[6]),
                             content_type='application/json')
    assert b'Invalid' in response.data
    assert response.status_code == 400

def test_update_orders_no_orders(client):
    response = client.put('/api/v1/orders/1', data=json.dumps(json_data[2]),
                             content_type='application/json')
    assert b'error' in response.data
    assert response.status_code == 404

def test_update_orders_not_exists(client):
    response = client.put('/api/v1/orders/4', data=json.dumps(json_data[2]),
                             content_type='application/json')
    assert b'error' in response.data
    assert response.status_code == 404

def test_get_menu_item_error(client):
    response = client.get('/api/v1/menu/4')
    assert response.status_code == 404
    assert b'error' in response.data

def test_get_menu_item(client):
    response = client.get('/api/v1/menu/1')
    assert response.status_code == 200
    assert b'Burger' in response.data

def test_get_orders_error(client):
    response = client.get('/api/v1/orders')
    assert b'sorry' in response.data
    assert response.status_code == 404


def test_orders_post_burger(client):
    response = client.post('/api/v1/orders', data=json.dumps(json_data[0]),
                             content_type='application/json')
    assert response.status_code == 201
    assert b'Burger' in response.data

def test_get_orders(client):
    response = client.get('/api/v1/orders')
    assert b'Burger' in response.data
    assert response.status_code == 200

def test_orders_post_chicken(client):
    response = client.post('/api/v1/orders', data=json.dumps(json_data[1]),
                             content_type='application/json')
    assert response.status_code == 404
    assert b'Error' in response.data

def test_orders_post_error_integer(client):
    response = client.post('/api/v1/orders', data=json.dumps({"Burger":""}),
                             content_type='application/json')
    assert response.status_code == 400
    assert b'Error' in response.data

def test_update_orders(client):
    response = client.put('/api/v1/orders/1', data=json.dumps(json_data[2]),
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

def test_get_menu(client):
    response = client.get('/api/v1/menu')
    assert b'menu_item' in response.data
    assert response.status_code == 200

def test_update_menu(client):
    response = client.put('/api/v1/menu/1', data=json.dumps(json_data[4]),
                             content_type='application/json')
    assert b'Ice Cream' in response.data
    assert response.status_code == 201

def test_update_menu_item_not_exist(client):
    response = client.put('/api/v1/menu/10', data=json.dumps(json_data[4]),
                             content_type='application/json')
    assert b'item does not exist' in response.data
    assert response.status_code == 404

def test_update_menu_error(client):
    response = client.put('/api/v1/menu/1', data=json.dumps({}),
                                content_type='application/json')
    assert b'Error' in response.data
    assert response.status_code == 400

def test_out_of_stock(client):
    response = client.post('/api/v1/orders', data=json.dumps(json_data[5]),
                            content_type='application/json')
    assert response.status_code == 404
    assert b'not on the menu' in response.data

def test_invalid_order(client):
    response = client.post('/api/v1/orders', data=json.dumps({}),
                            content_type='application/json')
    assert response.status_code == 400
    assert b'Error' in response.data

def test_add_menu_item_error(client):
    response = client.post('api/v1/menu', data=json.dumps({"error":2}),
                            content_type='application/json')
    assert response.status_code == 400
    assert b'Error' in response.data

def test_update_order_error(client):
    response = client.put('api/v1/orders/1', data=json.dumps({"error":"error"}),
                            content_type='application/json')
    assert response.status_code == 400
    assert b'Error' in response.data
    