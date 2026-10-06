from test_data import *
from policy import POLICY


def is_allowed(key, role):
    return role in POLICY.get(key, [])


def json_search(key, input_object, role=None):
    ret_val = []
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                if role is None or is_allowed(k, role):
                    ret_val.append({k: v})
            if isinstance(v, dict):
                ret_val.extend(json_search(key, v, role))
            elif isinstance(v, list):
                for item in v:
                    if not isinstance(item, (str, int)):
                        ret_val.extend(json_search(key, item, role))
    else:
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val.extend(json_search(key, val, role))
    return ret_val
