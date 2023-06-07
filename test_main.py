from fastapi.testclient import TestClient

from main import app

client = TestClient(app) 

def test_get_questions():
    response = client.post(
        "/quiz/",
        json={"questions_num": 0}
    )
    assert response.status_code == 200
