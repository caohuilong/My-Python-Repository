import requests
import time

url = "http://192.168.56.103:32705/base/heartbeat"
gamecore6 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore3 = ["gamecore1", "gamecore2", "gamecore4"]
gamecore12 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6", "gamecore7", "gamecore8", "gamecore9", "gamecore10", "gamecore11", "gamecore12"]

while True:
    for node in gamecore6:
        data = {"namespace": "default", "rayClusterName": "raycluseter-autoscale", "name": node,
                "nodeType": "gamecore", "clusterId": "SL"}
        response = requests.post(url, json=data)
        print(node, "heartbeat request Status code:", response.status_code, response.content)

    time.sleep(60)
    print("\n")