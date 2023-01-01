import requests
import time


url = "https://www.google.com"
t_begin = time.time()

r = requests.get(url)

t_end = time.time()

print(int(round((t_end - t_begin) * 1000)))
