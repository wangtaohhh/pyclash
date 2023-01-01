import yaml_analysis

# necessary infomation
data = yaml_analysis.airport_data
proxy_groups = data["proxy-groups"]
group_num = len(proxy_groups)  # how many groups do you have


group_name_list = [proxy_groups[i]["name"] for i in range(group_num)]

server_info_list = [proxy_groups[i]["proxies"] for i in range(group_num)]
