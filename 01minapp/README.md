
docker image build -t flask .

docker run -p 5001:80 -v ${PWD}/app:/app -d flask

docker exec -it 87b6ff8a302d sh

http://0.0.0.0:5001/get1
