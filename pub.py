import paho.mqtt.client as mqtt
import time
import datetime

# alamat broker menggunakan IP address
broker_address = "172.16.18.80"

# membuat client baru
print("creating new instance")
client = mqtt.Client("P1")

# menyambungkan publish ke broker dengan port=3333
print("connecting to broker", broker_address)
client.connect(broker_address,port=3333)

client.loop_start()

for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    client.publish("time", str(datetime.datetime.now()) + " " + str(i))

print("read file")

# membuka file bernama "exo.jpg"
f = open('exo.jpg','rb')
# membaca file
content = f.read()
# mengubah file menjadi byte
file = bytes(content)

print("sending file")

# mempublish topic
client.publish("photo",file)
# menutup file
f.close()

print("file uploaded")