import pytest
import json
from app import app, create_table, save_to_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            create_table()
        yield client

def test_publish_data(client):
    data = {
        'Instances': {
            'id1': {'pos_x': 10.0, 'pos_y': 20.0}
        },
        'timestamp': {'$date': {'$numberLong': '1700390400000'}}
    }
    response = client.post('/publish', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['status'] == 'success'

def test_get_data(client):
    data = {
        'Instances': {
            'id1': {'pos_x': 10.0, 'pos_y': 20.0}
        },
        'timestamp': {'$date': {'$numberLong': '1700390400000'}}
    }
    save_to_db(data)

    response = client.get('/api/data')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_get_heatmap(client):
    data = {
        'Instances': {
            'id1': {'pos_x': 10.0, 'pos_y': 20.0},
            'id2': {'pos_x': 15.0, 'pos_y': 25.0}
        },
        'timestamp': {'$date': {'$numberLong': '1700390400000'}}
    }
    save_to_db(data)

    response = client.get('/api/heatmap')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0