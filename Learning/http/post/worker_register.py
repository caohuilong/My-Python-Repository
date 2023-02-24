import requests

url = "http://192.168.56.103:32705/base/register"

workers = ["worker1", "worker2", "worker3"]
weights = [10, 20, 30]
for i in [2]:
    data = {"namespace": "default", "rayClusterName": "raycluseter-autoscale", "name": workers[i],
            "nodeType": "worker", "weight": weights[i]}
    response = requests.post(url, json=data)
    print(workers[i], "register request Status code:", response.status_code, response.content.decode("utf-8"))
