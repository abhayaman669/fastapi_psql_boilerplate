"""
Testing test route
"""

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_read_main():
    """
    Function to test route
    """
    res = client.get("/test")
    data = res.json()
    assert res.status_code == 200
    assert data == {'status': 'Success.', 'message': 'Hello World!'}
