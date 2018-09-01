# -*- coding: utf-8 -*-

import sys
import json
import time
from Splatoon_API import *


def test_result_parser():
    results = sys.stdin
    results_dict = json.load(results)

    r = Result_Parser(results_dict)
    print r.get_header()
    print r.get_header_csv_fmt()
    print r.get_data()
    print r.get_data_csv_fmt().encode("utf-8")

def test_splatoon_api():
    api = Splatoon_API()
    #api.get_iksm_session()
    r = Result_Parser(api.get_results())
    print r.get_header_csv_fmt()
    print r.get_data_csv_fmt().encode("utf-8")
    


test_splatoon_api()
