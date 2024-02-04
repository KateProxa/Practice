from fastapi.testclient import TestClient #import PyTest
from translator import app #import app from translator.py

client = TestClient(app) #creation of a client for testing

# function below is testing an accessibility of an app while adressing to the root catalogue on server 
def test_read_main():
    response = client.get("/predict/") # request HTTP GET to the /predict/ directory and save the result into variable response
    assert response.status_code == 200 # code 200 means that ruquest was successful. Other codes will mean that smth is wrong
    assert response.json() == {"message": "hello world"}# this test check response contents. If it equals "hello world"



