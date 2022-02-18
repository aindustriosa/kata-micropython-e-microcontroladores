# Kata de Micropython e microcontroladores - 1ª Edición

O obxectivo da sesión e de aprender sobre [Micropython](https://micropython.org/) e a sua integración coa
placa [TTGO ESP32](https://makeradvisor.com/esp32-sx1276-lora-ssd1306-oled/), unha placa que dispoñe de
Wifi e unha pequena pantalla OLED.

## Duración

90 minutos. Unha vez finalizados podemos compartir os avances e quen queira pode continuar explorando.

## Material a utilizar nesta sesión

* [TTGO ESP32 LoRa](https://makeradvisor.com/esp32-sx1276-lora-ssd1306-oled/)
* Sensor temperatura, humidade e presión [BME280](https://www.adafruit.com/product/2652)

## Entorno de traballo

Idealmente previamente configurado antes da actividade, se non o configuraremos
durante a mesma.

* É necseario un IDE compatible con ESP32.
  * O máis sinxelo e instalar [Thonny](https://thonny.org/),
  * Tamén podedes optar por [VSCode](https://code.visualstudio.com/) pero require a instalación de
extensións e o uso de ferramentas externas.

## Actividade

1. Nos xuntaremos en grupos de duas persoas, soámente é necesario un ordenador
por grupo pero podedes traballar en paralelo se o preferides.

2. Actualizar o firmware da placa e probar Micropython.

3. Empezaremos a traballar co obxectivo de ler do sensor e mostrar na pantalla os valores.
  [Mapa de conexións do sensor BM280](./recursos/bm280_connectivity_map.jpg)

4. Unha vez finalizado o punto anterior, e de maneira optativa, enviar unha pull request co noso
proxecto asignando un nome o equipo.

5. O terminar, podemos continuar polo camiño queiramos, ¿enviar os datos a un servizo remoto?
¿Mellorar a interface na pantalla?
