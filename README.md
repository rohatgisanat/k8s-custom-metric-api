sudo docker build -t custom-metrics-api:0.0.7 .
sudo docker save custom-metrics-api:0.0.7 > custom-metrics-api.tar
microk8s ctr image import custom-metrics-api.tar
helm install custom-metrics-api custom-metrics-api/  -n custom-metrics-api