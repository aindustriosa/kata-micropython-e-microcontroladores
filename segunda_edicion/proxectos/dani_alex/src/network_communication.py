import network
from umqtt.simple import MQTTClient

#Wifi
ssid='<wifi_SSID>'
wifi_password='<contrasinal>'

def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, wifi_password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    print('is connected')


#MQTT
mqtt_server = 'test.mosquitto.org'
client_id = "<custom_client_id>"

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server,  keepalive=30)
    client.connect()
    return client

