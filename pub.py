import paho.mqtt.client as mqtt

import time
import datetime

broker_address = "192.168.1.3"

print("creating new instance")
client = mqtt.Client("P1")

print("connecting to broker", broker_address)
client.connect(broker_address,port=3333)

print("read file")

f = open('exo.jpg','rb')

content = f.read()

file = bytes(content)

print("publish foto")
client.publish("photo",file)

client.loop_start()

for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    client.publish("waktu", str(datetime.datetime.now()) + " " + str(i))

f.close()
print("file uploaded")