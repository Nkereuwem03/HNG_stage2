from API.models import Person


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {'message': 'tests route'}


def test_create_person(client, app):
    response = client.post('/api', json={"person": "nkereuwem udoudo"})
    assert response.status_code == 200
    assert response.json == {'Message': 'Created Successfully'}
    with app.app_context():
        assert Person.query.first().name == 'nkereuwem udoudo'


def test_create_person_wrong_json_schema(client):
    response = client.post('/api', json={"persons": 1})
    assert response.status_code == 500
    assert response.json == {'Message': 'Create Error'}


def test_get_person(client):
    response = client.get('/api/1')
    assert response.status_code == 200


def test_get_non_existent_person(client):
    response = client.get('/api/100')
    assert response.status_code == 404
    assert response.json == {'Message': 'Not Found'}


def test_update_person(client, app):
    response = client.put('/api/1', json={"person": "nkereuwem"})
    assert response.status_code == 200
    assert response.json == {'Message': 'Update Successful'}
    with app.app_context():
        assert Person.query.first().name == 'nkereuwem'


def test_update_person_wrong_json_schema(client):
    response = client.put('/api/1', json={"person": 1})
    assert response.status_code == 500
    assert response.json == {'Message': "Update Error"}


def test_update_non_existent_person(client):
    response = client.put('/api/100')
    assert response.status_code == 404
    assert response.json == {'Message': 'Not Found'}


def test_delete_person(client):
    response = client.delete('/api/1')
    assert response.status_code == 200
    assert response.json == {'Message': 'Deleted Successfully'}


def test_delete_non_existent_person(client):
    response = client.delete('/api/100')
    assert response.status_code == 404
    assert response.json == {'Message': 'Not Found'}
