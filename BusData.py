from pykafka import KafkaClient
import json
import datetime
import time

#Read in bus data
input_file=json.load(open('bus1.json'))
coordinates=input_file['features'][0]['geometry']['coordinates']



client = KafkaClient(hosts="localhost:9092")

topic=client.topics['geodata_final']

producer = topic.get_sync_producer()

for i in coordinates:
    data ={
        'busline':'0001',
        'timestep':str(datetime.datetime.now()),
        'latitude':i[0],
        'longitude':i[1]
        }
    message=json.dumps(data)
    print(message)
    time.sleep(1)
    producer.produce(str(message).encode('ascii'))