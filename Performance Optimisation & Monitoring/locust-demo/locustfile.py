import json
from locust import HttpUser, TaskSet, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def call_predict(self):
        payload = {
            "feature1": 1.5,
            "feature2": 2.5
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/predict", data=json.dumps(payload), headers=headers)

    @task
    def home(self):
        self.client.get("/")