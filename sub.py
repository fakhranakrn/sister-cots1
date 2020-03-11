import paho.mqtt.client as mqtt
import time
import datetime
import socket

def on_message(client, userdata, message):
    # tulis nama file dengan "myidol.jpg"
    f = open('myidol.jpg','wb')
    f.write(message.payload)
    f.close()
    
    # menyimpan history waktu pengiriman message ke 'history.txt'
    t = open('history.txt','a')
    t.write(str(message.payload.decode("utf-8")))
    t.write("\n")
    t.close()

# alamat broker menggunakan IP address
broker_address = "192.168.137.29"

# melihat IP asal subscriber
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Subscriber IP:",host_ip)

# membuat client baru
print("creating new instance")
client = mqtt.Client("P2")

# menyambungkan subscriber ke broker dengan port=3333
print("connecting to broker")
client.connect(broker_address, port=3333)

client.loop_start()

# subscribe topic "photo" dan "time"
print("Subscribing to topic")
client.subscribe([("photo",1),("waktu",2)])

client.on_message=on_message

while True:
    time.sleep(1)

client.loop_stop()