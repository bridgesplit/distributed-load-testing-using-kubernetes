import uuid

from datetime import datetime
from locust import FastHttpUser, TaskSet, task
        
class BsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(10)
    def basic(self):
        self.client.get("/launchpad/v1/num_minted_collection_by_stage/4fCwYtv87dBtTxMmZP569RyrkXW7cwgojFf9rr17TsHb")
        self.client.get("/launchpad/v1/user_whitelist/4fCwYtv87dBtTxMmZP569RyrkXW7cwgojFf9rr17TsHb/eLxrJn888nqseqChe5LVijP73PtKzzDg2JdGi2EEtgP")
        self.client.get("/launchpad/v1/collection_by_name/text_collection_kazc177")
        self.client.get("/launchpad/v1/available/4fCwYtv87dBtTxMmZP569RyrkXW7cwgojFf9rr17TsHb")


class MetricsLocust(FastHttpUser):
    tasks = {BsTaskSet}