#### Usage: pass json file to Test_Result_Parser.py
#### Ex. cat result.json | python Test_Result_Parser.py

# -*- coding: utf-8 -*-

import sys
import json
from Result_Parser import Result_Parser

results = sys.stdin
results_dict = json.load(results)

r = Result_Parser(results_dict)
#print r.get_header()
print r.get_header_csv_fmt()
#print r.get_data()
print r.get_data_csv_fmt().encode("utf-8")
