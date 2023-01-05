import requests


def save_subscription(url):

    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.149 Safari/537.36"
    }

    url_clash_flag_list = url.split("&")

    # build url for clash
    if url_clash_flag_list[-1] != "flag=clash":
        url = url_clash_flag_list[0] + "&flag=clash"

    r = requests.get(url=url, headers=head)
    with open("subscription.yaml", "w", encoding="utf8") as f:
        f.write(r.text)
    return "finished"


if __name__ == "__main__":

    save_subscription('https://welink345.233.tw/api/v1/client/subscribe?token=84884bb5dbfdfad03e30102df39cf81f')

# save_subscription()
