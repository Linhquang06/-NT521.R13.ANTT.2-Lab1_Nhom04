from test_data import *

def json_search(key, input_object):
    ret_val = []
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                ret_val.append({k: v})
            if isinstance(v, dict):
                ret_val.extend(json_search(key, v))
            elif isinstance(v, list):
                for item in v:
                    if not isinstance(item, (str, int)):
                        ret_val.extend(json_search(key, item))
    else:
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val.extend(json_search(key, val))
    return ret_val
