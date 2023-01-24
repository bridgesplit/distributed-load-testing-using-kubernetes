import uuid

from datetime import datetime
from locust import FastHttpUser, TaskSet, task
        
class BsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(10)
    def basic(self):
        self.client.get("/launchpad/v1/num_minted_collection_by_stage/78DBRykF32fTcUwXL2kXUpm2xNREDn6rZG2Drb4bCKbL")
        self.client.get("/launchpad/v1/user_whitelist/5exd6i2LavtJ7CRAhwnuhbPjYQGERFxe9zREZpDj5Lay/HooKEmrXGx2BdRi3A3GJA1KqKoJQwdqXCBmLnNUbX9LV")
        self.client.get("/launchpad/v1/collection_by_name/test_mint_43")
        self.client.get("/launchpad/v1/available/78DBRykF32fTcUwXL2kXUpm2xNREDn6rZG2Drb4bCKbL")


class MetricsLocust(FastHttpUser):
    tasks = {BsTaskSet}