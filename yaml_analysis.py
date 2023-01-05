import imp
import yaml
import os

# if os.path.exists('subscription.yaml'):
    
yaml_file = open("subscription.yaml", "r", encoding="utf8")

airport_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

# print(airport_data)
