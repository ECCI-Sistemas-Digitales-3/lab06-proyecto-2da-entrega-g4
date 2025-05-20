import machine, time, network, config
from umqtt.simple import MQTTClient

#MQTT Topics
MQTT_TOPIC_TEMPERATURE = 'temperatura/sensor/DS18B20'

# MQTT Parametros
MQTT_SERVER = b'192.168.140.47'
MQTT_PORT = 1883
MQTT_USER = None
MQTT_PASSWORD = None
MQTT_CLIENT_ID = b"rpi_picow_Alejo"
MQTT_KEEPALIVE = 7200
MQTT_SSL = False   # set to False if using local Mosquitto MQTT broker
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}

def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    #Conexion con Red Wi-Fi
    wlan.connect(ssid, password)
    #Esperamos 10 Segundos pa la Conexion
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('...Esperando Conexion Wi-Fi...')
        time.sleep(1)
    #Comprobamos la Conexion Wi-Fi
    if wlan.status() != 3:
        return False
    else:
        print('Conexion Exitosa!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

def connect_mqtt():
    try:
        client = MQTTClient(client_id=MQTT_CLIENT_ID,
                            server=MQTT_SERVER,
                            port=MQTT_PORT,
                            user=MQTT_USER,
                            password=MQTT_PASSWORD,
                            keepalive=MQTT_KEEPALIVE,
                            ssl=MQTT_SSL,
                            ssl_params=MQTT_SSL_PARAMS)
        client.connect()
        return client
    except Exception as e:
        print('Error de Conexion con MQTT:', e)
        raise  # Re-raise the exception to see the full traceback

def publish_mqtt(topic, value):
    client.publish(topic, value)
    print(topic)
    print(value)
    print("Publish Done")

try:
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error de Conexion con Red Wi-Fi...')
    else:
        #Conectamos con MQTT Broker y iniciamos MQTT Client
        client = connect_mqtt()
        temperature = 0
        while True:
            #Publicamos el mensaje por MQTT
            publish_mqtt(MQTT_TOPIC_TEMPERATURE, str(temperature))
            temperature += 1
            time.sleep(10)

except Exception as e:
    print('Error:', e)