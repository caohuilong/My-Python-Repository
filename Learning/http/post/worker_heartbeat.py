import requests
import time

url = "http://apps-new-danlu-vm-dev.danlu.netease.com:44888/base/heartbeat"
workers = ["worker1", "worker2", "worker3"]

while True:
    for node in workers:
        data = {"namespace": "default", "rayClusterName": "raycluseter-test", "name": node,
                "nodeType": "worker"}
        response = requests.post(url, json=data)
        print(node, "heartbeat request Status code:", response.status_code, response.content.decode("utf-8"))

    time.sleep(60)
    print("\n")