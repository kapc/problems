#! /usr/env/python

def flatten_dict(input_val, result_dict, parent_key):
    print(input_val)
    if not isinstance(input_val, dict):
        result_dict[parent_key] = input_val
        return
    for key, value in input_val.items():
        result_key = "{}.{}".format(parent_key, key) if parent_key else key
        flatten_dict(value, result_dict, result_key)

def compare_dict(actual, expected):
    actual_dict = {}
    expected_dict = {}
    result = []

    flatten_dict(actual, actual_dict, "")
    flatten_dict(expected, expected_dict, "")

    actual_keys = set(actual_dict.keys())
    expected_keys = set(expected_dict.keys())

    added_keys = actual_keys - expected_keys
    removed_keys = expected_keys - actual_keys
    common_keys = actual_keys & expected_keys

    for key in added_keys:
        result.append(['+', key, actual_dict[key]])
    for key in removed_keys:
        result.append(['-', key, expected_dict[key]])

    for key in common_keys:
        actual_value = actual_dict[key]
        expected_value = expected_dict[key]

        if actual_value != expected_value:
            result.append(['+', key, actual_dict[key]])
            result.append(['-', key, expected_dict[key]])
    return result

expected = {'a' : 2, 'b' : {'c' : {'d' : 3}}}
actual = {'a' : 1}

print(compare_dict(expected, actual))



