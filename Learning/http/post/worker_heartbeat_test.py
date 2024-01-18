import requests
import time

url = "http://apps-sl.danlu.netease.com:35890/base/heartbeat"
workers = ["ray-dch-0-8cf6bc45f-kdfxw"]

while True:
    for node in workers:
        data = {"namespace": "1000-daicanhuang-part-1111", "rayClusterName": "raycluseter-test", "name": node,
                "nodeType": "worker"}
        response = requests.post(url, json=data)
        print(node, "heartbeat request Status code:", response.status_code, response.content.decode("utf-8"))

    time.sleep(60)
    print("\n")