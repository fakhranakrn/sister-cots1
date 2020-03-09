import paho.mqtt.client as mqtt

import time
import datetime

def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "surf.jpg"
    f = open('myidol.jpg','wb')
    f.write(message.payload)
    
    #data = str(message.payload)
    #f.write(data)
    f.close()

    print("message received ",str(message.payload.decode("utf-8")))

broker_address="192.168.1.3"

print("creating new instance")
client = mqtt.Client("P2")

print("connecting to broker", broker_address)
client.connect(broker_address, port=3333)

print("Subscribing to topic")
client.subscribe([("photo",1),("waktu",2)])


# loop forever
# while True:
#     # berikan waktu tunggu 1 detik 
#     time.sleep(1)

client.on_message=on_message

while True:
    client.loop(15)
    time.sleep(2)