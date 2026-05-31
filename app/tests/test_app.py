def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200


def test_health_response(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'ok'


def test_ready(client):
    response = client.get('/ready')
    assert response.status_code == 200


def test_results(client):
    response = client.get('/results')
    assert response.status_code == 200


def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200


def test_vote_csk(client):
    response = client.post('/vote/chennai-super-kings')
    assert response.status_code in [200, 404]


def test_vote_mi(client):
    response = client.post('/vote/mumbai-indians')
    assert response.status_code in [200, 404]


def test_vote_rcb(client):
    response = client.post('/vote/royal-challengers-bengaluru')
    assert response.status_code in [200, 404]