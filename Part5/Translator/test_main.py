from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_empty_text():
    response = client.post("/predict/", json={"text": ""})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == "C'est ce que j'ai dit."

def test_empty_json():
    response = client.post("/predict/", json={})
    json_data = response.json()
    assert response.status_code == 422
    assert json_data['detail'][0]['type'] == "missing"
    assert json_data['detail'][0]['msg'] == "Field required"


