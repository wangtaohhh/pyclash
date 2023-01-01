from operator import contains
import yaml_analysis

data = yaml_analysis.airport_data
proxies_dict_ls_in_proxy_groups = data["proxy-groups"]


def change_all_proxy_groups(server_name) -> list:  # all proxies-group
    """
    :param server_name: server name is the server which is choosed, the func will delete others
    """
    for (
        server_info_group
    ) in proxies_dict_ls_in_proxy_groups:  # a list contains some dict

        proxies_in_group_new = []

        for server in server_info_group["proxies"]:
            if server == server_name:
                proxies_in_group_new.append(server)
            else:
                pass

        # emm.... if find nothing
        if len(proxies_in_group_new) == 0:
            proxies_in_group_new.append(
                server_info_group["proxies"][-1]
            )  # choose one randomly

        # print(proxies_in_group_new)
        server_info_group["proxies"] = proxies_in_group_new
    # print(proxies_dict_ls_in_proxy_groups)

    return proxies_dict_ls_in_proxy_groups


if __name__ == "__main__":
    print(change_all_proxy_groups("🇯🇵 [负载均衡]日本"))
