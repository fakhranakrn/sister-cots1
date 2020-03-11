import paho.mqtt.client as mqtt
import time
import datetime
import socket

# alamat broker menggunakan IP address
broker_address = "192.168.137.29"
# membuat client baru
print("creating new instance")
client = mqtt.Client("P1")

# melihat IP asal publisher
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Publisher IP:",host_ip)

# menyambungkan publish ke broker dengan port=3333
print("connecting to broker")
client.connect(broker_address,port=3333)

client.loop_start()

# mempublish topic time
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    client.publish("waktu", str(datetime.datetime.now()))

print("read file")

# membuka file bernama "exo.jpg"
f = open('exo.jpg','rb')
# membaca file
content = f.read()
# mengubah file menjadi byte
file = bytes(content)

print("sending file")

# mempublish topic photo
client.publish("photo",file)
# menutup file
f.close()

print("file uploaded")