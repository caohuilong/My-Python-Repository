import requests

url = "http://apps-sl.danlu.netease.com:35890/base/register"
gamecore6 = ["gamecore1", "gamecore2", "gamecore3", "gamecore4", "gamecore5", "gamecore6"]
gamecore2 = ["gamecore3", "gamecore4", "gamecore6"]
gamecore3 = ["gamecore1", "gamecore6", "gamecore4"]
gamecore1 = ["gamecore3", "gamecore5"]
gamecore0 = ["gamecore1"]

for node in gamecore1:
    data = {"namespace": "1000-daicanhuang-part-1111", "rayClusterName": "raycluseter-test", "name": node,
            "nodeType": "gamecore", "clusterId": ""}
    response = requests.post(url, json=data)
    print(node, "register request Status code:", response.status_code, response.content.decode("utf-8"))
