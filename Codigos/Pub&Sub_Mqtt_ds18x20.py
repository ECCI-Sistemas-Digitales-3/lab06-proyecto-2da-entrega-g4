# - machine: para acceder a los pines y hardware del microcontrolador.
# - time: para manejar esperas y tiempos de ejecución.
# - network: para conexión Wi-Fi.
# - config: módulo separado que contiene las credenciales Wi-Fi.
# - onewire, ds18x20: para leer sensores DS18B20 usando el protocolo OneWire.
# - umqtt.simple: cliente MQTT para publicar y suscribirse a mensajes.
import machine, time, network, config, onewire, ds18x20
from umqtt.simple import MQTTClient

# Definimos los temas (topics) MQTT donde se publicará la temperatura
MQTT_TOPIC_PUB_TEMPERATURE = [
    'temperatura/sensor/DS18B20/1',
    'temperatura/sensor/DS18B20/2',
    'temperatura/sensor/DS18B20/3',
    'temperatura/sensor/DS18B20/4',
    'temperatura/sensor/DS18B20/5'
]

# Definimos los temas a los que el dispositivo se suscribirá para recibir comandos de control
MQTT_TOPIC_SUB_RESISTENCIAS = [
    'temperatura/control/1',
    'temperatura/control/2',
    'temperatura/control/3',
    'temperatura/control/4',
    'temperatura/control/5'
]

# Parámetros para la conexión MQTT
MQTT_SERVER = b'192.168.196.47'        # Dirección IP del servidor MQTT (broker)
MQTT_PORT = 1883                       # Puerto por defecto de MQTT
MQTT_USER = None                       # Usuario (no se usa en este caso)
MQTT_PASSWORD = None                   # Contraseña (no se usa en este caso)
MQTT_CLIENT_ID = b"rpi_picow_Alejo"    # Identificador único para este cliente MQTT
MQTT_KEEPALIVE = 7200                  # Tiempo para mantener viva la conexión
MQTT_SSL = False                       # No usamos SSL ya que es una red local
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}  # Parámetros SSL (no usados)

# Sección para configurar sensores DS18B20
ds_pin = machine.Pin(22)                           # Definimos el pin GPIO22 para el bus OneWire
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))  # Inicializamos comunicación con sensores
roms = ds_sensor.scan()                            # Escaneamos para detectar los sensores conectados
number_devices = len(roms)                         # Contamos cuántos sensores fueron encontrados

# Se sobrescribe la lista de sensores con sus direcciones específicas (ROMs)
roms = [
    b'\x28\xd7\x6a\x84\x00\x00\x00\x24',
    b'\x28\xc1\xe8\x34\x00\x00\x00\x14',
    b'\x28\x5b\x5c\x38\x00\x00\x00\x28'
]

# Mostramos por consola cuántos sensores fueron encontrados y sus direcciones
print('Numero de sensores= ', number_devices)
print('Direccion= ', roms)

def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Creamos interfaz Wi-Fi en modo estación
    wlan.active(True)                    # Activamos la interfaz Wi-Fi
    wlan.connect(ssid, password)         # Intentamos conectar con SSID y contraseña

    connection_timeout = 10              # Esperamos máximo 10 segundos para conexión
    while connection_timeout > 0:
        if wlan.status() >= 3:           # Si se conecta correctamente (status >= 3)
            break
        connection_timeout -= 1
        print('...Esperando Conexion Wi-Fi...')
        time.sleep(1)

    if wlan.status() != 3:               # Si después de intentar, no se conecta
        return False                     # Indicamos que falló
    else:
        print('Conexion Exitosa!')
        network_info = wlan.ifconfig()   # Mostramos IP asignada
        print('IP address:', network_info[0])
        return True

def connect_mqtt():
    try:
        client = MQTTClient(
            client_id=MQTT_CLIENT_ID,
            server=MQTT_SERVER,
            port=MQTT_PORT,
            user=MQTT_USER,
            password=MQTT_PASSWORD,
            keepalive=MQTT_KEEPALIVE,
            ssl=MQTT_SSL,
            ssl_params=MQTT_SSL_PARAMS
        )
        client.connect()                # Intentamos conectar al broker MQTT
        return client                   # Si fue exitoso, retornamos el cliente
    except Exception as e:
        print('Error de Conexion con MQTT:', e)
        raise                          # Re-lanzamos el error para diagnóstico

def publish_mqtt(topic, value):
    client.publish(topic, value)       # Publicamos el valor en el topic especificado
    print(topic)
    print(value)
    print("Publish Done")


def subscribe(client, topic):
    client.subscribe(topic)            # Nos suscribimos al topic MQTT
    print('Subscribe to topic:', topic)

def my_callback(topic, message):
    print('Topic: ', topic)
    print('msg: ', message)

    # Verificamos qué comando se recibió y respondemos
    if topic == b'temperatura/control/1':
        if message == b'ON':
            print('Resistencia 1 ON')
        elif message == b'OFF':
            print('Resistencia 1 OFF')
        else:
            print('Comando sin Reconocer')

    elif topic == b'temperatura/control/2':
        if message == b'ON':
            print('Resistencia 2 ON')
        elif message == b'OFF':
            print('Resistencia 2 OFF')
        else:
            print('Comando sin Reconocer')

    elif topic == b'temperatura/control/3':
        if message == b'ON':
            print('Resistencia 3 ON')
        elif message == b'OFF':
            print('Resistencia 3 OFF')
        else:
            print('Comando sin Reconocer')

    elif topic == b'temperatura/control/4':
        if message == b'ON':
            print('Resistencia 4 ON')
        elif message == b'OFF':
            print('Resistencia 4 OFF')
        else:
            print('Comando sin Reconocer')

    elif topic == b'temperatura/control/5':
        if message == b'ON':
            print('Resistencia 5 ON')
        elif message == b'OFF':
            print('Resistencia 5 OFF')
        else:
            print('Comando sin Reconocer')

    else:
        print('Topic sin Reconocer')

try:
    # Primero nos conectamos a la red Wi-Fi usando datos del archivo config.py
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error de Conexion con Red Wi-Fi...')
    else:
        # Si la conexión Wi-Fi fue exitosa, conectamos al servidor MQTT
        client = connect_mqtt()
        client.set_callback(my_callback)  # Registramos la función para manejar mensajes entrantes

        # Nos suscribimos a cada uno de los topics de control de resistencias
        for rom in range(number_devices):
            subscribe(client, MQTT_TOPIC_SUB_RESISTENCIAS[rom])
            time.sleep(0.2)  # Pequeña pausa entre suscripciones

        while True:
            # Pedimos a los sensores que realicen la conversión de temperatura
            ds_sensor.convert_temp()
            time.sleep_ms(750)  # Esperamos el tiempo necesario para que termine

            for rom in range(number_devices):
                # Leemos la temperatura del sensor actual
                tempC = ds_sensor.read_temp(roms[rom])
                print("Sensor N° {}, Temperatura = {:.2f}".format(rom+1, tempC))
                print()

                # Enviamos la temperatura a través de MQTT al topic correspondiente
                publish_mqtt(MQTT_TOPIC_PUB_TEMPERATURE[rom], str(tempC))
                time.sleep(0.5)
                client.check_msg()  # Revisamos si hay mensajes nuevos entrantes

            print('Temperaturas Publicadas')                
            time.sleep(5)  # Esperamos 5 segundos antes de repetir el ciclo

except Exception as e:
    print('Error:', e)

# Conección del microcontrolador a una red Wi-Fi.

# Conexión a un broker MQTT en la red local.

# Escaneo de sensors DS18B20, lectura de sus temperaturas y publicacion vía MQTT.

# Recibimiento de comandos desde el servidor MQTT para controlar resistencias (ON/OFF).

