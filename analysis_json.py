import json

with open("subscription.json", 'r') as f:
    a = json.load(f)
    # print(a)

len_dict = len(a)
dict_keys = list(a.keys())
dict_values = list(a.values())

# print(len_dict)