import os
import requests
print("os path:", os.getcwd())

json = {
    "mes": [{
        "key1": "anantha",
        "name": "anantha"
    },
     {
        "key2": "kumar",
        "name": "kumar"
      }
    ]
}

for i, val in enumerate(json["mes"]):
    print(i)
    print(val)

url = 'http://www.google.com/blahblah'

try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()

except Exception as err:
    print(err.__str__())


"""
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh.__str__())
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
"""