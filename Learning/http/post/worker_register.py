import requests

url = "http://apps-new-danlu-vm-dev.danlu.netease.com:44888/base/register"
# url = "http://apps-sl.danlu.netease.com:35890/base/register"

workers = ["worker1", "worker2", "worker3"]
weights = [5, 5, 5]
for i in [0, 1, 2]:
    data = {"namespace": "default", "rayClusterName": "raycluseter-test", "name": workers[i],
            "nodeType": "worker", "weight": weights[i]}
    response = requests.post(url, json=data)
    print(workers[i], "register request Status code:", response.status_code, response.content.decode("utf-8"))
