import pytest
from flask import json
from app import create_app
from manage import APP
from flask_jwt_extended import JWTManager

json_data = [
    {
	"username":"NewAdmin",
	"email":"admin@example.com",
	"password":"adminpassword",
	"role":"admin"
    },
    {
	"username":"NewAdmin",
    "password":"adminpassword"
    },
    {
    "username":"error",
    "password":"error"
    },
    {
    "username":"NewUser",
    "password":"error"
    },
    {
	"username":"NewUser",
    "password":"userpassword"
    },
    {
	"username":"NewUser",
	"email":"user@example.com",
	"password":"userpassword",
	"role":"user"
    },
    {
	"username":"'ErrorData'",
	"email":"'error@example.com'",
	"password":"'errorpassword'",
	"role":"'error'"
    },
    {
	"menu_item": "IceCream",
	"description": "Flavor Full and creamy",
	"price": 200
    },
    {
	"menu_item": "'IceCream'",
	"description": "'Flavor Full and creamy'",
	"price": 200
    },
    {
    "IceCream":3
    },
    {
    "IceCream":"3"
    },
    {
    "Milk":3,
    "Meat":3
    }
    ]

@pytest.fixture
def client(request):    
    app = create_app('testing') 
    JWTManager(app)
    test_client = app.test_client()   
    return test_client

@pytest.fixture
def get_admin_token(client):
    response = client.post('/auth/login', data=json.dumps(json_data[1]),
                             content_type='application/json')
    token = json.loads(response.data)['token']
    print(token)
    header = {
        'Authorization':'Bearer {0}'.format(token)
    }
    return header

@pytest.fixture
def get_user_token(client):
    response = client.post('/auth/login', data=json.dumps(json_data[4]),
                             content_type='application/json')
    token = json.loads(response.data)['token']
    print(token)
    header = {
        'Authorization':'Bearer {0}'.format(token)
    }
    return header


def test_create_admin(client):
    response = client.post('/auth/users', data=json.dumps(json_data[0]),
                             content_type='application/json')
    assert b'Success' in response.data

def test_create_user(client):
    response = client.post('/auth/users', data=json.dumps(json_data[5]),
                             content_type='application/json')
    assert b'Success' in response.data

def test_login(client):
    response = client.post('/auth/login', data=json.dumps(json_data[1]),
                             content_type='application/json')
    assert b'token' in response.data

def test_get_users(client, get_admin_token):
    response = client.get('/auth/users', headers=get_admin_token)
    assert b'Users' in response.data
    assert response.status_code == 200

def test_get_single_user(client, get_admin_token):
    response = client.get('/auth/users/1', headers=get_admin_token)
    assert b'User' in response.data
    assert response.status_code == 200

def test_get_single_user_no_admin(client, get_user_token):
    response = client.get('/auth/users/1', headers=get_user_token)
    assert b'Route restricted' in response.data
    assert response.status_code == 403

def test_login_error(client):
    response = client.post('/auth/login', data=json.dumps(json_data[2]),
                             content_type='application/json')
    assert b'Could not verify' in response.data
    assert response.status_code == 401

def test_login_no_password(client):
    response = client.post('/auth/login', data=json.dumps(json_data[3]),
                             content_type='application/json')
    assert b'Invalid Password' in response.data
    assert response.status_code == 401

def test_get_users_no_admin(client, get_user_token):
    response = client.get('/auth/users', headers=get_user_token)
    assert b'admin only' in response.data
    assert response.status_code == 403

def test_create_user_no_data(client):
    response = client.post('/auth/users', data=json.dumps({}),
                             content_type='application/json')
    assert b'You did not enter data correctly' in response.data
    assert response.status_code == 400

def test_create_user_no_error_data(client):
    response = client.post('/auth/users', data=json.dumps(json_data[6]),
                             content_type='application/json')
    assert b'Syntax Error' in response.data
    assert response.status_code == 400


def test_add_menu_items(client, get_admin_token):
    response = client.post('/api/v2/menu', headers=get_admin_token,
                             data=json.dumps(json_data[7]),
                             content_type='application/json')
    assert b'Success' in response.data
    assert response.status_code == 201

def test_view_menu_new_item(client):
    response = client.get('/api/v2/menu')
    assert b'Menu' in response.data
    assert response.status_code == 200

def test_add_menu_items_no_admin(client, get_user_token):
    response = client.post('/api/v2/menu', headers=get_user_token,
                             data=json.dumps(json_data[7]),
                             content_type='application/json')
    assert b'restricted to admin' in response.data
    assert response.status_code == 403

def test_add_menu_items_error(client, get_admin_token):
    response = client.post('/api/v2/menu', headers=get_admin_token,
                             data=json.dumps(json_data[8]),
                             content_type='application/json')
    assert b'SyntaxError' in response.data
    assert response.status_code == 400

def test_add_menu_items_no_data(client, get_admin_token):
    response = client.post('/api/v2/menu', headers=get_admin_token,
                             data=json.dumps({}),
                             content_type='application/json')
    assert b'you did not enter data correctly' in response.data
    assert response.status_code == 400

def test_place_order(client, get_user_token):
    response = client.post('/api/v2/orders', headers=get_user_token,
                             data=json.dumps(json_data[9]),
                             content_type='application/json')
    assert b'Success' in response.data
    assert response.status_code == 201

def test_place_order_syntax_error(client, get_user_token):
    response = client.post('/api/v2/orders', headers=get_user_token,
                             data=json.dumps(json_data[10]),
                             content_type='application/json')
    assert b'SyntaxError' in response.data
    assert response.status_code == 400

def test_place_order_error_out_of_stock(client, get_user_token):
    response = client.post('/api/v2/orders', headers=get_user_token,
                             data=json.dumps(json_data[11]),
                             content_type='application/json')
    assert b'following items are not on the menu' in response.data
    assert response.status_code == 404

def test_get_all_orders(client, get_admin_token):
    response = client.get('/api/v2/orders', headers=get_admin_token)
    assert b'Orders' in response.data
    assert response.status_code == 200

def test_get_all_orders_no_admin(client, get_user_token):
    response = client.get('/api/v2/orders', headers=get_user_token)
    assert b'Only admin allowed' in response.data
    assert response.status_code == 403





