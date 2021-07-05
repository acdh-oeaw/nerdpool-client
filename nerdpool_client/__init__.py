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
    
    def yield_samples(self, dataset_title=False, limit=False, **kwargs):
        """ iterator to yield all ner-samples
        :param dataset_title: Title of a specific dataset
        :type dataset_title: str
        :param limit: Bool to flag if only a short sample\
        of samples should be fetched, defaults to `False`
        :type limit: bool
        :return: An iterator yielding abbreviations
        :rtype: iterator
        """
        params = []
        print(kwargs)
        next = True
        if dataset_title:
            params.append(('ner_source__title', dataset_title))
        if kwargs:
            for key, value in kwargs.items():
                params.append((key, value))
        
        url = self.sample_ep
        counter = 0
        if limit:
            max_samples = 5
        while next:
            response = requests.get(url, params=params)
            print(response.url)
            result = response.json()
            if result.get('next', False):
                url = result.get('next')
            else:
                next = False
            results = result.get('results')
            for x in results:
                counter += 1
                if limit:
                    if counter <= max_samples:
                        next = False
                        yield(x)
                else:
                    yield(x)
