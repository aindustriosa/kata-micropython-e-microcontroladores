from machine import Pin, SoftI2C
import time
from time import sleep
import bme280_float as bme280   #https://github.com/robert-hh/BME280
import ssd1306
from network_communication import mqtt_connect, wifi_connect


led_onboard = Pin(2, Pin.OUT) #built-in blue LED
led_onboard.value(1)

pin_reset = Pin(16, Pin.OUT)
pin_reset.value(0)
sleep(0.001)
pin_reset.value(1)

i2c = SoftI2C(scl=Pin(15), sda=Pin(4), freq=400000, timeout=255)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

bme = bme280.BME280(i2c=i2c)

wifi_connect()
mqtt_client = mqtt_connect()
topic_pub = 'aindustriosa'


while True:
    t,p,h=bme.values #strings returned, for raw values use read_compensated_data
    temp=f'Temp: {t}'
    press=f'Press: {p}'
    hum=f'Hum: {h}'
    year, month, day, hour, minutes, seconds, *_ = time.gmtime()
    date_time = f'{year}-{month}-{day}-{hour}:{minutes}:{seconds}'
    print('date:', date_time)
    oled.fill(0)
    oled.text('A Industriosa',12,50)
    oled.text(temp,0,0)
    oled.text(press,0,10)
    oled.text(hum,0,20)
    oled.text(date_time,0,30)
    oled.show()

    mqtt_client.publish(f'{topic_pub}/temp', f'{t}')
    mqtt_client.publish(f'{topic_pub}/press', f'{p}')
    mqtt_client.publish(f'{topic_pub}/hum', f'{h}')
    # led_onboard.value(not led_onboard.value())
    sleep(10)
    
c.disconnect()
