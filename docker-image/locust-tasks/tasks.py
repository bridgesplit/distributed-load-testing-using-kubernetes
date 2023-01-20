import uuid

from datetime import datetime
from locust import FastHttpUser, TaskSet, task
        
class BsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(10)
    def basic(self):
        self.client.get("/launchpad/v1/stage/21bVUE7tMyqkzHcnWeLca45PFUwkwLU47578GQFKpfpD")
        self.client.get("/launchpad/v1/whitelist/EdNcP1gw4si8VUrRyP2BnaSV9H971gF9tawDhLbboZv5")
        # self.client.get("/user/nfts_without_meta/7bz4h6T4p39ozCnz7vpDmmiFNssyV1d1Hu3TKcDXmSXu")
        self.client.get("/launchpad/v1/collection_by_name/chipfunks")
    @task(1)
    def force(self):
        self.client.get("/launchpad/v1/stage/21bVUE7tMyqkzHcnWeLca45PFUwkwLU47578GQFKpfpD?force=true")


class MetricsLocust(FastHttpUser):
    tasks = {BsTaskSet}