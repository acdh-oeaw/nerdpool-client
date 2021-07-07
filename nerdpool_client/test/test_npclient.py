import json
import types
import os


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
ENDPOINT = "https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-sample"
JSONL_DUMP = "hansi4ever_out.jsonl"


class TestNerdPoolClient(TestCase):

    def test_data_sets(self):
        data_sets = client.data_sets
        self.assertTrue(isinstance(data_sets, list))

    def test_str(self):
        self.assertEqual(f"{client}", "Nerdpool API Client")

    def test_sample_to_json(self):
        item = client.sample_to_json(SAMPLE_JSON)
        self.assertEqual(len(item.keys()), 2)

    def test_yield_samples(self):
        data = client.yield_samples(ENDPOINT, limit=True)
        self.assertTrue(isinstance(data, types.GeneratorType))
        self.assertTrue(len([x for x in data]), 5)

    def test_dump_to_jsonl(self):
        try:
            os.remove(JSONL_DUMP)
        except FileNotFoundError:
            pass
        dump = client.dump_to_jsonl(ENDPOINT,  limit=True, file_name=JSONL_DUMP)
        self.assertEqual(dump, JSONL_DUMP)
        with open(JSONL_DUMP, "r") as f:
            sample = json.loads(f.readline())
            self.assertTrue('text' in sample.keys())
        os.remove(JSONL_DUMP)
