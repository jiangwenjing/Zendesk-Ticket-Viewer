#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Wenjing Jiang
"""

import requests
from requests.auth import HTTPBasicAuth


class Query:
    def __init__(self, user, password, url):
        self.user = user
        self.password = password
        self.url = url
        self.ret_list = []
        self.ret_dict = {}
        self.query()

    # connect api
    def query(self):
        try:
            response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password))
            # if connect success, get the data
            if response.status_code == 200:
                ret = response.json()
                self.ret_list = ret["requests"]
                for ele in ret["requests"]:
                    self.ret_dict[ele["id"]] = ele
        # catch error
        except BaseException as e:
            print("connect error:{}".format(repr(e)))

    # display all tickets
    def show_all(self, page_num):
        try:
            if self.ret_list:
                # calculate tickets in every page
                start = (int(page_num)-1)*25
                end = int(page_num)*25 if int(page_num)*25 <= len(self.ret_list) else len(self.ret_list)
                print("id", "\t", "subject")
                for ele in self.ret_list[start:end]:
                    print(ele["id"], "\t", ele["subject"])
        # catch error
        except BaseException as e:
            print("get tickets error:{}".format(repr(e)))

    # display ticket detail
    def show_detail_by_id(self, _id):
        try:
            if self.ret_dict:
                for key, value in self.ret_dict[int(_id)].items():
                    if key == "description":
                        value = value.replace("\n", "")
                    print(key, ": ", value)
        # catch error
        except BaseException as e:
            print("get ticket detail error:{}".format(repr(e)))
