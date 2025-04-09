from machine import Pin, SoftI2C, ADC, PWM
import network, neopixel
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
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

pin_neopixel = Pin(5)
neo = neopixel.NeoPixel(pin_neopixel,8)

servo_pin = Pin(4)
servo = PWM(servo_pin,freq=50)
servo.duty(20)

for i in range(8):
    neo[i] = (32, 0, 0)    
neo.write()

pin_reset = Pin(16, Pin.OUT)
pin_reset.value(0)
sleep_ms(10)
pin_reset.value(1)

i2c = SoftI2C(scl=Pin(15), sda=Pin(4), freq=400000, timeout=255)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sta_if = network.WLAN(network.STA_IF)


while True:
    if not sta_if.isconnected():
        do_connect(SSID,PASS)    #WIP: some issues with first connection attempt should be fixed
    ip,mask,gate,ext_ip=sta_if.ifconfig()
    pot_value = pot.read()
    pot_perc = pot_value/4096*100
    pot_perc_5 = pot_perc - (pot_perc % 5)
    str1=f'Pot: {int(pot_perc_5)}'
    numero_caracteres = pot_perc // 10
    str2 = ''
    for i in range (numero_caracteres):
        str2=str2+'#'
    str4=f'IP: {ip}'
    oled.fill(0)
    oled.text(str1,0,0)
    oled.text(str2,0,10)
    oled.text(str4,0,50)
    oled.show()
    numero_pixels = pot_perc // 11.11111
    print(pot_perc)
    print(numero_pixels)
    neo.fill((0,0,0))

    if(numero_pixels <= 4):
        for i in range(3, int(numero_pixels) - 1, -1):
            neo[i] = (0, 16, 0)
    else:
        for i in range(4,int(numero_pixels), 1):
            neo[i] = (0, 16, 0)
    neo.write()

    led_onboard.value(not led_onboard.value())
    sleep(0.5)