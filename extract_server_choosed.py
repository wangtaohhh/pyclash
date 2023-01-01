import yaml_analysis

data = yaml_analysis.airport_data
proxies_dict_ls = data["proxies"]  # a list


def extract_server_info(server_name) -> list:
    """
    parameter is the name of the server , and then return the server information
    :param server_name: the name of the server
    :return: information list of "proxies"
    """
    proxies_user_choose = []
    for proxies_dict in proxies_dict_ls:
        # print(proxies_dict['name'])
        if proxies_dict["name"] == server_name:
            proxies_user_choose.append(proxies_dict)

    if (
        len(proxies_user_choose) == 0
    ):  # if cannot find the server name, the func will return the first server in this airport
        proxies_user_choose.append(proxies_dict_ls[-1])
    return proxies_user_choose


if __name__ == "__main__":
    print(extract_server_info("🇯🇵 [负载均衡]日本"))
