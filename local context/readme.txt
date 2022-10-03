How to build and run the container I use and the URL for Spark UI where we can monitor how the program is executing and look for bottlenecks

#build container from Dockerfile
sudo docker build -t context/pyspark .


#run notebook with Laurence's local storage 
sudo docker run -p 8888:8888 -p 4040:4040 -v  /home/laurence/WiFiProject:/home/jovyan/work --gpus all  context/pyspark 
##run notebook without local storage
sudo docker run -p 8888:8888 jupyter/pyspark-notebook

#Spark UI
http://0.0.0.0:4040/





`

