# OBXETIVO

Como continuación do traballado na sesión previa (letura do sensor BM280), nesta ocasión o obxetivo e enviar datos por [MQTT](https://mqtt.org/) a un servidor remoto. No presente exemplo estamos a usar o servidor de probas facilitado por https://test.mosquitto.org/ onde figuran os detalles para a conexión.

O código fonte está na carpeta `src`.

```
    src/
        umqtt/ # Librería MQTT (https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html)
        bme280_float.py # Librería da pantalla
        network_communication.py # Ficheiro cos datos para conexión Wifi e MQTT
        main.py
        sd1306.py # Librería da pantalla
```

Tanto a configuración para a conexión Wifi e MQTT e necesario editar os valores a man no
ficheiro `network_communication.py`

Para comprobar a publicación en MQTT pódese utilizar o client [mosquitto](https://mosquitto.org/download/) compatible para as distintas plataformas.

Se o código se executa corretamente, con o seguinte comando podeste suscribir as publicacións:

`~ mosquitto_sub -h test.mosquitto.org -t "aindustriosa/#" -u wildcard -v`
