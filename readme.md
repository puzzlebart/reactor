# Reactor core Template
This is a template to generate the Docker images used when creating new nuclear reactors in Springfield.

## Minimal path to awesome
* Make sure you have docker installed and running. More information [here](https://docs.docker.com/docker-for-windows/install/).
* Run `docker build -t reactor_core_docker_flask:latest`
* Run `docker run -d -p 5000:5000 reactor_core_docker_flask:latest`
* Navigate to http://127.0.0.1:5000/


## Api endpoints
* / : Reactor core information
    * id: the unique id of the nuclear core instance
    * created: the date when the core was created
* /temperature: reactor core temperature information
    * temperature: the current temperature of the reactor
    * last_update: the date of the last temperature update