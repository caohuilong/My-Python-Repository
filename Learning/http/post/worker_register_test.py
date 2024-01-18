import requests

# url = "http://apps-new-danlu-vm-dev.danlu.netease.com:44888/base/register"
url = "http://apps-sl.danlu.netease.com:35890/base/register"

workers = ["ray-dch-0-8cf6bc45f-kdfxw", "worker2", "worker3"]
weights = [10, 20, 30]
for i in [0]:
    data = {"namespace": "1000-daicanhuang-part-1111", "rayClusterName": "raycluseter-test", "name": workers[i],
            "nodeType": "worker", "weight": weights[i],"port": 22}
    response = requests.post(url, json=data)
    print(workers[i], "register request Status code:", response.status_code, response.content.decode("utf-8"))
