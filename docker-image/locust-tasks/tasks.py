from locust import FastHttpUser, task

class BSApis(FastHttpUser):
    @task
    def basic(self):
        self.client.get("/launchpad/v1/stage/21bVUE7tMyqkzHcnWeLca45PFUwkwLU47578GQFKpfpD")
        self.client.get("/launchpad/v1/whitelist/EdNcP1gw4si8VUrRyP2BnaSV9H971gF9tawDhLbboZv5")
        self.client.get("/launchpad/v1/available/EdNcP1gw4si8VUrRyP2BnaSV9H971gF9tawDhLbboZv5")
        self.client.get("/launchpad/v1/collection_by_name/chipfunks")
        