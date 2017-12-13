# geohackery

This repository consists of many Jupyter Notebook snippets from [Geohackweek 2016](http://geohackweek.github.io/) and [Earth Engine User Summit 2017](https://events.withgoogle.com/google-earth-engine-user-summit-2017/).

For using the Earth Engine Python API, the best option currently includes using docker to control the development environment.

**[Docker Key Terms](https://docs.docker.com/get-started/)**
- *Image*: lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

- *Container*: runtime instance of an image—what the image becomes in memory when actually executed. It runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

#### Instructions

1. Download **Docker for Windows**
2. Open Windows PowerShell as Administrator <br>

Pull docker images:
> docker pull geohackweek2016/docker-ee-datascience-notebook

Show all docker containers:
> docker ps -a

Start docker container:
> docker start [container_alias]

Stop docker container:
> docker stop [container_alias]

Restart docker container:
> docker container restart [container_alias]

Bind notebooks to environment:
> docker run -d -p 8888:8888 --name docker-ee-datascience-notebook -v "C:/geohackweek/ee_docker/work:/home/jovyan/work" -v "C:/geohackweek/ee_docker/.config/earthengine:/home/jovyan/.config/earthengine" geohackweek2016/docker-ee-datascience-notebook

Restart docker:
>"C:/geohackweek/ee_docker/work> docker restart docker-ee-datascience-notebook

Launch Jupyter notebook:

2 METHODS ):
> **A)** C:/geohackweek/ee_docker/work>
docker run geohackweek2016/docker-ee-datascience-notebook

> **B)** --C:/geohackweek/ee_docker/work> jupyter notebook--

*To-Do*<br>
Use docker container with additional libraries for visualization of geospatial data in Jupyter Notebooks.
- IPyLeaflet, GeoPandas, Folium (wrapper on Leaflet)

Here are a few interesting libraries which could be the start of interactive mapping using the Earth Engine Python API
1. [IPyLeaflet](https://github.com/ellisonbg/ipyleaflet)
2. [Folium GEE](https://github.com/mccarthyryanc/folium_gee) binding with [Folium](https://github.com/mccarthyryanc/folium_gee)
