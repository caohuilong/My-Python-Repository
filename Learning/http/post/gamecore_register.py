import requests

url = "http://apps-new-danlu-vm-dev.danlu.netease.com:44888/base/register"
gamecore9 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6", "gamecore7", "gamecore8", "gamecore9"]
gamecore6 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore2 = ["gamecore3", "gamecore4", "gamecore6"]
gamecore3 = ["gamecore1", "gamecore6", "gamecore4"]
gamecore1 = ["gamecore3", "gamecore5"]
gamecore0 = ["gamecore6"]

for node in gamecore0:
    data = {"namespace": "default", "rayClusterName": "raycluseter-test", "name": node,
            "nodeType": "gamecore", "clusterId": ""}
    response = requests.post(url, json=data)
    print(node, "register request Status code:", response.status_code, response.content.decode("utf-8"))
