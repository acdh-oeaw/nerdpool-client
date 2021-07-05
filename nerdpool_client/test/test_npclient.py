from unittest import TestCase

from nerdpool_client import NerdPoolClient


class TestNerdPoolClient(TestCase):

    def test_data_sets(self):
        client = NerdPoolClient()
        data_sets = client.data_sets
        self.assertTrue(isinstance(data_sets, list))