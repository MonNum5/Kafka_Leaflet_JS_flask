# Discription
This follows the Kafka JS Flask [tutorial from youtube](https://www.youtube.com/watch?v=vD9Ic8KqEDw&amp;list=PL2UmzTIzxgL7Bq-mW--vtsM2YFF9GqhVB&amp;index=7) for streaming gps data via kafka and display the results
on a geographical map hosted with a flask app

# Files

File / Folder | Description
--- | --- 
BusData.py | read in data and start producer
app.py | flask app and consumer
templates | html templates with JS code
bus1.json | gps data that gets streamed

# Installation 
Install [Kafka](https://kafka.apache.org/quickstart) and follow the description given on the website of the mentioned you tube video

pip install -r requirements.txt

# Run
Start zookeeper
Create topic
python BusData.py
python app.py
