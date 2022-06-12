version: "3.8"
services:
    selenium-hub:
        image: selenium/hub
        container_name: selenium-hub
        ports:
            - "4444:4444"
   
    chrome:
        image: selenium/node-chrome
        volumes:
            - /dev/shm:/dev/shm
        depends_on:
            - selenium-hub
        environment:
            - HUB_PORT_4444_TCP_ADDR=selenium-hub
            - HUB_PORT_4444_TCP_PORT=4444
            - NODE_MAX_INSTANCES=3
        ports:
            -" 6900:5900"