import requests


NP_BASE_URL = "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/"


class NerdPoolClient():

    def __init__(self, base_url=NP_BASE_URL):
        self.base_url = base_url
        self.endpoints = self.fetch_endpoints()
        self.data_set_ep = self.endpoints['ner-source']
        self.sample_ep = self.endpoints['ner-sample']
        self.data_sets = self.list_data_set_titles()

    def __str__(self):
        return "Nerdpool API Client"

    def fetch_endpoints(self):
        r = requests.get(self.base_url)
        return r.json()

    def fetch_data_sets(self):
        r = requests.get(self.data_set_ep)
        return r.json()['results']

    def list_data_set_titles(self):
        return [x['title'] for x in self.fetch_data_sets()]
