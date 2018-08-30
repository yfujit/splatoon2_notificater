#### Parse result dictionary to list format
# -*- coding: utf-8 -*-

import json

class Result_Parser:
    def __init__(self, results_dict):
        self._header = ["battle_number", "my_team_result", "player_rank", 
                        "rule", "udemae", "estimate_gachi_power", 
                        "game_paint_point", "kill_count", "assist_count", 
                        "death_count", "special_count", "stage", "weapon"
                        ]
        self._data = None
        self._data = self.parse_results(results_dict)

    def get_data(self):
        return self._data

    def get_data_csv_fmt(self):
        r_val = ""
        for d in self._data:
            r_val = r_val + ",".join(d) + "\n"
        return r_val

    def get_header(self):
        return self._header

    def get_header_csv_fmt(self):
        return ",".join(self._header)

    def parse_result(self, result_dict):
        data_dict = {}
        data_dict["battle_number"]     = result_dict["battle_number"]
        data_dict["my_team_result"]    = result_dict["my_team_result"]["name"]
        data_dict["player_rank"]       = str(result_dict["player_rank"])
        data_dict["rule"]              = result_dict["rule"]["name"]
        if "udemae" in result_dict:
            data_dict["udemae"]               = result_dict["udemae"]["name"]
            data_dict["s_plus_number"]        = result_dict["udemae"]["s_plus_number"]
            if data_dict["udemae"] == "S+": data_dict["udemae"] += str(data_dict["s_plus_number"])
        else:
            data_dict["udemae"]       = "null"
        if "estimate_gachi_power" in result_dict:
            data_dict["estimate_gachi_power"] = str(result_dict["estimate_gachi_power"])
        else:
            data_dict["estimate_gachi_power"] = "null"
        player_result                 = result_dict["player_result"]
        data_dict["game_paint_point"] = str(player_result["game_paint_point"])
        data_dict["kill_count"]       = str(player_result["kill_count"])
        data_dict["assist_count"]     = str(player_result["assist_count"])
        data_dict["death_count"]      = str(player_result["death_count"])
        data_dict["special_count"]    = str(player_result["special_count"])
        data_dict["stage"]            = result_dict["stage"]["name"]
        data_dict["weapon"]           = player_result["player"]["weapon"]["name"]
        data_list = []
        for key in self._header:
            data_list.append(data_dict[key])

        return data_list

    def parse_results(self, results_dict):
        data_list = []
        for result in results_dict["results"]:
            data_list.append(self.parse_result(result))
        return data_list
