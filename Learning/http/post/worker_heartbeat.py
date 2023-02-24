import requests
import time

url = "http://192.168.56.103:32705/base/heartbeat"
workers = ["worker1", "worker2", "worker3"]
workers2 = ["worker1", "worker2"]

while True:
    for node in workers:
        data = {"namespace": "default", "rayClusterName": "raycluseter-autoscale", "name": node,
                "nodeType": "worker"}
        response = requests.post(url, json=data)
        print(node, "heartbeat request Status code:", response.status_code, response.content.decode("utf-8"))

    time.sleep(60)
    print("\n")