
import pytest
from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def test_index(client):
    response = client.get('/api/v1/orders')
    assert response.status_code == 200

def test_users_post(client):
    response = client.post('api/v1/orders?item=Burger&quantity=2')
    assert response.status_code == 201