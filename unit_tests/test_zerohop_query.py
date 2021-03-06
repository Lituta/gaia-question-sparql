import unittest
import sys
import os
sys.path.append('../')
from src.zerohop_query import ZerohopQuery
from src.query_tool import QueryTool, Mode

base_path = os.path.dirname(__file__)
zq = ZerohopQuery(base_path + '/sample_queries/zerohop_queries.xml')
ttl_path = base_path + '/sample_ttls/doc1.ttl'


class TestZerohopQuery(unittest.TestCase):
    def test_zerohop_singleton(self):
        qt = QueryTool(ttl_path, Mode.SINGLETON)
        responses, stat, errors = zq.ask_all(qt)
        self.assertFalse(errors)
        self.assertEqual(len(responses), 3)

    def test_zerohop_cluster(self):
        qt = QueryTool(ttl_path, Mode.CLUSTER)
        responses, stat, errors = zq.ask_all(qt)
        self.assertFalse(errors)
        self.assertEqual(len(responses), 3)

    def test_zerohop_prototype(self):
        qt = QueryTool(ttl_path, Mode.PROTOTYPE)
        responses, stat, errors = zq.ask_all(qt)
        self.assertFalse(errors)
        self.assertEqual(len(responses), 3)

