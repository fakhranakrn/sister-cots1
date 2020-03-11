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
    t = open('history.txt','a')
    t.write(str(message.payload.decode("utf-8")))
    t.write("\n")
    t.close()

    # t = open("history.txt","w")
    # for i in range(20):
    #     t.write("message received ",str(message.payload.decode("utf-8")))
    #     t.write("\n")
    # t.close()

# alamat broker menggunakan IP address
broker_address="192.168.137.29"

# membuat client baru
print("creating new instance")
client = mqtt.Client("P2")

# menyambungkan subscriber ke broker dengan port=3333
print("connecting to broker", broker_address)
client.connect(broker_address, port=3333)

client.loop_start()

# subscribe topic "photo" dan "time"
print("Subscribing to topic")
client.subscribe([("photo",1),("waktu",2)])

# t = open('history.txt','w')
client.on_message=on_message
# t.close()

while True:
    time.sleep(1)

client.loop_stop()