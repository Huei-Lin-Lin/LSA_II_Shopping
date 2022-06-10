app="gchrome_app:latest"
chrome="selenium/standalone-chrome:latest"
docker-compose build
docker run -d -p 5000:5000 ${app}
docker run -d -p 4444:4444 --shm-size="2g" ${chrome}