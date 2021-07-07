import json
from unittest import TestCase

from nerdpool_client import NerdPoolClient

client = NerdPoolClient()
SAMPLE_JSON = json.loads("""{
    "url": "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-sample/55084/?format=json",
    "ner_text": "Votant könne daher nur dem Antrage des Staatsratspräsidenten beipflichten.",
    "ner_sample": {
        "text": "Votant könne daher nur dem Antrage des Staatsratspräsidenten beipflichten.",
        "entities": [
            [39, 60, "PER"]
        ]
    },
    "ner_ent_exist": true,
    "ner_ent_type": "PER",
    "ner_source": "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-source/9/?format=json"
}""")


class TestNerdPoolClient(TestCase):

    def test_data_sets(self):
        data_sets = client.data_sets
        self.assertTrue(isinstance(data_sets, list))

    def test_str(self):
        self.assertEqual(f"{client}", "Nerdpool API Client")

    def test_sample_to_json(self):
        item = client.sample_to_json(SAMPLE_JSON)
        self.assertEqual(len(item.keys()), 2)
