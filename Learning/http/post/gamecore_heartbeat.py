import requests
import time

url = "http://apps-new-danlu-vm-dev.danlu.netease.com:44888/base/heartbeat"
gamecore9 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6", "gamecore7", "gamecore8", "gamecore9"]
gamecore6 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore3 = ["gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore5 = ["gamecore3", "gamecore6", "gamecore7", "gamecore8", "gamecore9"]

while True:
    for node in gamecore5:
        data = {"namespace": "default", "rayClusterName": "raycluseter-test", "name": node,
                "nodeType": "gamecore", "clusterId": "DEV"}
        response = requests.post(url, json=data)
        print(node, "heartbeat request Status code:", response.status_code, response.content)

    time.sleep(60)
    print("\n")