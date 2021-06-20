from flask import Flask
import json
from datetime import datetime
app = Flask(__name__)

@app.route("/apis/custom.metrics.k8s.io/v1beta1")
def list1():
    return "okay";
@app.route("/apis/custom.metrics.k8s.io/v1beta1/namespaces/custom-metrics-api/services/custom-metrics-api/second")
def list():
    data = json.loads( open ('metricValueList.json', "r").read())
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    print(timestamp)
    data["items"][0]["timestamp"]=timestamp
    return data;

if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context='adhoc')