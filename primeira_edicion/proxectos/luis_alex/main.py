from machine import Pin, SoftI2C
import network
from time import sleep_ms, sleep
import bme280_float as bme280   #https://github.com/robert-hh/BME280
import ssd1306
import urequests as requests
import json
from env_var import url, headers, SSID, PASS

def do_connect(SSID, PASSWORD):
    print('Conectando a la red', SSID +"...")
    sta_if.active(True)                       
    try:
        sta_if.connect(SSID, PASSWORD)
        print('Configuración de red (IP/netmask/gw/DNS):', sta_if.ifconfig())
    except Exception as e:
        print("ERROR: ",str(e))
    
led_onboard = Pin(2, Pin.OUT) #built-in blue LED
led_onboard.value(1)

pin_reset = Pin(16, Pin.OUT)
pin_reset.value(0)
sleep_ms(10)
pin_reset.value(1)

i2c = SoftI2C(scl=Pin(15), sda=Pin(4), freq=400000, timeout=255)
print (i2c.scan()) #I2C test

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sta_if = network.WLAN(network.STA_IF)

bme = bme280.BME280(i2c=i2c)

while True:
    if not sta_if.isconnected():
        do_connect(SSID,PASS)    #WIP: some issues with first connection attempt should be fixed
    ip,mask,gate,ext_ip=sta_if.ifconfig()
    t,p,h=bme.values #strings returned, for raw values use read_compensated_data
    str1=f'Temp: {t}'
    str2=f'Press: {p}'
    str3=f'Hum: {h}'
    str4=f'IP: {ip}'
    oled.fill(0)
    oled.text(str1,0,0)
    oled.text(str2,0,10)
    oled.text(str3,0,20)
    oled.text(str4,0,50)
    oled.show()
    temp,press,hum=bme.read_compensated_data()
    print (temp)
    data = [
            {"variable": "temperature",
            "value": temp,
            "unit":"C"},
            {"variable": "humidity",
            "value": hum,
            "unit":"%"},
            {"variable": "pressure",
            "value": press,
            "unit":"hPa"},
            ]
    results = {"data": None, "errors": None}
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers)
        results = r.json()
    except Exception as e:
        print ("ERROR: ",str(e))
        results["errors"]=str(e)
    print(results)
    
    led_onboard.value(not led_onboard.value())
    sleep(60)