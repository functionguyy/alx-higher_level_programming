#!/usr/bin/python3
def best_score(a_dictionary):

    if type(a_dictionary) is dict:
        keys = a_dictionary.keys()

        if len(keys) > 0:
            best_score_key = ""
            best_score_value = 0
            for key in keys:
                value = a_dictionary[key]
                if value > best_score_value:
                    best_score_value = value
                    best_score_key = key
        else:
            return None

        return best_score_key

    else:
        return None
