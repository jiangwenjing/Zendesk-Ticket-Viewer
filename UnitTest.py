#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Wenjing Jiang
"""

import unittest
from Query import Query


class QueryTest(unittest.TestCase):
    def setUp(self):
        self.user = "wjiang@tcd.ie/token"
        self.password = "cdOVayx0Rp7S6kUQ64M9YG4BzaIP6OVFbQLhRMWv"
        self.url = "https://zcctcd.zendesk.com/api/v2/requests"

    # test query all tickets
    def test_show_all(self):
        qry = Query(self.user, self.password, self.url)
        for i in range(100):
            qry.show_all(i)

    # test query ticket detail
    def test_show_detail_by_id(self):
        qry = Query(self.user, self.password, self.url)
        for i in range(100):
            qry.show_detail_by_id(i)


if __name__ == '__main__':
    unittest.main()
