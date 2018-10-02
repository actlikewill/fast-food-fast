import pytest
from base64 import b64encode
from flask import json
from manage import APP

json_data = [
    {
	"username":"NewUser",
	"email":"user@example.com",
	"password":"userpassword",
	"role":"admin"
    },
    {
	"username":"Wilson",
    "password":"wilassword"
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
	"username":"Sam",
    "password":"sampassword"
    },
    
    ]

@pytest.fixture
def client(request):       
    test_client = APP.test_client()
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

def test_create_user(client):
    response = client.post('/auth/users', data=json.dumps(json_data[0]),
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
