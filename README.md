# WiFi-Anomaly-Detection
This is the Masters Course Final Project

It is investigating the Agean Wireless Intrusion Dataset 3
https://icsdweb.aegean.gr/awid/awid3

I use Machine Learning, to identify the attack packets and a built a simple endpoint in Django.
I started off doing my analysis in Pyspark, then moved to Scikit-Learn

Local Contex - has the docker file and the commands to run and build the container, this was from Ubuntu

1 ETL - deals with null values cleans some errors and convers to Parquet

2 Random Forest Grid Search - I ran a random forest grid search on each attack to find the most important features

3 Tuning on a subsample - Before working on the cloud I wanted to try some tuning on a small stratified sample so I could get results and feedback in a reasonable time.

4 This has the Model run on the whole dataset in GCP on a Vertex AI managed workbook 16CPU 108gb RAM and a small model for testing my Django app

Django I made a simple django app with a REST API that makes and stores predictions based on my model. My starting point was an app I made for the cloud computing module.


