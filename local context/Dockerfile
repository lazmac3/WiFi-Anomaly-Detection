# starting point was https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f#9927
ARG BASE_CONTAINER=jupyter/pyspark-notebook
FROM $BASE_CONTAINER
LABEL author="Laurence Tickell"
USER root
# Switch back to jovyan 
USER $NB_UID
