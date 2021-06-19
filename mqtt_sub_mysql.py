import paho.mqtt.client as mqtt  # https://pypi.org/project/paho-mqtt/
import MySQLdb  # https://pypi.org/project/mysqlclient/

'''
    Change Variabel
'''
# MQTT
broker_address = "broker.emqx.io"
port = 1883
topic = "same/topic"

# MySql
db_address = 'localhost'
db_user = 'root'
db_pass = ''
db_name = 'tess'


def on_message(client, userdata, msg):
    value = msg.payload.decode("utf-8").split("-")

    # queryInsert = "INSERT INTO " + \
    #     value[0]+" VALUES (CURRENT_TIMESTAMP()," + value[1] + ","+value[2]+")"

    queryInsert = "INSERT INTO tableName VALUES ("+value+")"
    insertrec.execute(queryInsert)
    db.commit()
    # print(queryInsert)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("broker connect")
        print("Ready Save Data")
    else:
        print("failed connect broker")


def mqtt_main(client):
    '''
        MQTT Setting
    '''
    client.on_connect = on_connect
    client.on_message = on_message

    print("connecting to broker")
    client.connect(broker_address, port, 60)  # connect to broker
    client.subscribe(topic)
    return client


try:
    print("Start service")
    print("to Stop service press CTRL + C\n")

    db = MySQLdb.connect(db_address, db_user, db_pass, db_name)
    insertrec = db.cursor()

    client = mqtt.Client()  # create new instance
    client = mqtt_main(client)
    client.loop_forever()
except KeyboardInterrupt:
    db.close()
    print("")
    print("Stop recieve data")
except MySQLdb._exceptions.OperationalError as e:
    print(e)
