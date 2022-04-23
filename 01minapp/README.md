
docker image build -t flask .

docker run -p 5001:80 -v ${PWD}/app:/app -d flask


http://0.0.0.0:5001/get1
