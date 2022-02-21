#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Wenjing Jiang
"""

from Query import Query
import math


def main():
    print("Loading,please wait...")

    # connect api
    user = "wjiang@tcd.ie/token"
    password = "cdOVayx0Rp7S6kUQ64M9YG4BzaIP6OVFbQLhRMWv"
    url = "https://zcctcd.zendesk.com/api/v2/requests"

    qry = Query(user, password, url)

    # calculate maximum page number
    max_page_num = int(math.ceil(len(qry.ret_list)/25))
    # get all id
    id_list = [str(ele) for ele in qry.ret_dict.keys()]

    while True:
        try:
            option = input("menu\n* press 1 to view all tickets\n* press 2 to view a ticket details\n* type 'exit' to exit\n>")
            # view all tickets
            if option == '1':
                while True:
                    # page scope
                    page_num = input("page from %s to %s,press page number>" % (str(1), str(max_page_num)))
                    # if pressed page number is valid, show all the tickets in the page
                    if page_num in [str(ele) for ele in range(1, max_page_num+1)]:
                        qry.show_all(page_num)
                        print("type 'return' to return menu\n")
                    # return menu
                    elif page_num == "return":
                        print("return menu\n")
                        break
                    # if pressed page number is invalid, remind press again or return to menu
                    else:
                        print("invalid page number, press again, or type 'return' to return menu\n")
                        continue
            # view ticket detail
            elif option == '2':
                while True:
                    # id scope
                    _id = input('type id from %s to %s>' % (id_list[0], id_list[-1]))
                    # if typed id is valid, show the detail of the ticket
                    if _id in id_list:
                        qry.show_detail_by_id(_id)
                        print("type 'return' to return menu\n")
                    # return menu
                    elif _id == "return":
                        print("return menu")
                        break
                    # if typed id is invalid, remind type again or return menu
                    else:
                        print("invalid id,press again, or type 'return' to return menu\n")
                        continue
            # exit the program
            elif option == 'exit':
                print('exit\n')
                break
            # handle invalid option
            else:
                print('invalid option，type again\n')
        # catch error
        except BaseException as e:
            print("error,type again:{}\n".format(repr(e)))


if __name__ == '__main__':
    main()
