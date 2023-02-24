import requests

url = "http://192.168.56.103:32705/base/register"
gamecore6 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore2 = ["gamecore3", "gamecore5", "gamecore6"]
gamecore3 = ["gamecore1", "gamecore6", "gamecore4"]
gamecore1 = ["gamecore3", "gamecore5"]

for node in gamecore1:
    data = {"namespace": "default", "rayClusterName": "raycluseter-autoscale", "name": node,
            "nodeType": "gamecore", "clusterId": ""}
    response = requests.post(url, json=data)
    print(node, "register request Status code:", response.status_code, response.content.decode("utf-8"))
