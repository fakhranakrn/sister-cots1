import paho.mqtt.client as mqtt
import time
import datetime

def on_message(client, userdata, message):
    # tulis nama file dengan "myidol.jpg"
    f = open('myidol.jpg','wb')
    f.write(message.payload)
    f.close()
    # menampilkan waktu diterimanya message
    print("message received ",str(message.payload.decode("utf-8")))
    # t = open('history.txt','wb')
    # t.write("message received ",str(message.payload.decode("utf-8")))
    # t.close()

# alamat broker menggunakan IP address
broker_address="172.16.18.80"

# membuat client baru
print("creating new instance")
client = mqtt.Client("P2")

# menyambungkan subscriber ke broker dengan port=3333
print("connecting to broker", broker_address)
client.connect(broker_address, port=3333)

# subscribe topic "photo" dan "time"
print("Subscribing to topic")
client.subscribe([("photo",1),("time",2)])

client.on_message=on_message

while True:
    client.loop(15)
    time.sleep(2)