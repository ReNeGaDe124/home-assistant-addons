import requests
BASE_URL = "https://subs.ro/api/v1.0"
class SubsAPI:
    def __init__(self, api_key):
        self.headers = {"X-Subs-Api-Key": api_key}
    def search(self, field, value):
        r = requests.get(f"{BASE_URL}/search/{field}/{value}", headers=self.headers, params={"language":"ro"})
        r.raise_for_status()
        return r.json().get("items", [])
    def download(self, subtitle_id):
        r = requests.get(f"{BASE_URL}/subtitle/{subtitle_id}/download", headers=self.headers)
        r.raise_for_status()
        return r.content
