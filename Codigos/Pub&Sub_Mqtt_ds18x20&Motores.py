import machine, time, network, config, onewire, ds18x20
from umqtt.simple import MQTTClient

#MQTT Topics
MQTT_TOPIC_PUB_TEMPERATURE = ['temperatura/sensor/DS18B20/1','temperatura/sensor/DS18B20/2','temperatura/sensor/DS18B20/3','temperatura/sensor/DS18B20/4','temperatura/sensor/DS18B20/5']
MQTT_TOPIC_SUB_RESISTENCIAS = ['temperatura/control/1','temperatura/control/2','temperatura/control/3','temperatura/control/4','temperatura/control/5','motores/control/1','motores/control/2','motores/control/3','motores/control/4','motores/control/5','motores/control/reb']

# MQTT Parametros
MQTT_SERVER = b'192.168.227.47'
MQTT_PORT = 1883
MQTT_USER = None
MQTT_PASSWORD = None
MQTT_CLIENT_ID = b"rpi_picow_Alejo"
MQTT_KEEPALIVE = 7200
MQTT_SSL = False   # set to False if using local Mosquitto MQTT broker
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}

#Declaramos el pin que usaremos para la lectura y escritura
ds_pin = machine.Pin(20)
R1_pin = machine.Pin(28, machine.Pin.OUT)
R2_pin = machine.Pin(27, machine.Pin.OUT)
R3_pin = machine.Pin(26, machine.Pin.OUT)
R4_pin = machine.Pin(22, machine.Pin.OUT)
R5_pin = machine.Pin(21, machine.Pin.OUT)
reb = machine.Pin(0)
reb_pin = machine.PWM(reb)
M1_pin = machine.Pin(1, machine.Pin.OUT)
M2_pin = machine.Pin(2, machine.Pin.OUT)
M3_pin = machine.Pin(3, machine.Pin.OUT)
M4_pin = machine.Pin(4, machine.Pin.OUT)
M5_pin = machine.Pin(5, machine.Pin.OUT)
frequency = 5000
reb_pin.freq (frequency)


#Definimos la comunicacion por un solo cable
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
#Guardamos las direcciones de los sensores DS18B20
roms = ds_sensor.scan()
#Declaramos cuantos sensores tenemos
number_devices = len(roms)
roms = [b'\x28\xd7\x6a\x84\x00\x00\x00\x24',
        b'\x28\xc1\xe8\x34\x00\x00\x00\x14',
        b'\x28\x5b\x5c\x38\x00\x00\x00\x28',
        b'\x28\x34\xa3\x83\x00\x00\x00\x03',
        b'\x28\xa7\x4f\x38\x00\x00\x00\x15']
#Imprimimos la cantidad de sensores y sus direcciones
print('Numero de sensores= ', number_devices)
print('Direccion= ', roms)

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
    
#Subcribe a MQTT topics
def subscribe(client, topic):
    client.subscribe(topic)
    print('Subscribe to topic:', topic)

#Funcion que realiza al recibir un llamado
def my_callback(topic, message):
    #Imprimimos el Topic y el mensaje que recibimos
    print('Topic: ', topic)
    print('msg: ', message)
    
    if topic == b'temperatura/control/1':#Resistencia 1
        if message == b'ON':
            print('Resistencia 1 ON')#Encender Resistencia
            R1_pin.value(1)
        elif message == b'OFF':
            print('Resistencia 1 OFF')#Apagar Resistencia
            R1_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'temperatura/control/2':#Resistencia 2
        if message == b'ON':
            print('Resistencia 2 ON')#Encender Resistencia
            R2_pin.value(1)
        elif message == b'OFF':
            print('Resistencia 2 OFF')#Apagar Resistencia
            R2_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'temperatura/control/3':#Resistencia 3
        if message == b'ON':
            print('Resistencia 3 ON')#Encender Resistencia
            R3_pin.value(1)
        elif message == b'OFF':
            print('Resistencia 3 OFF')#Apagar Resistencia
            R3_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'temperatura/control/4':#Resistencia 4
        if message == b'ON':
            print('Resistencia 4 ON')#Encender Resistencia
            R4_pin.value(1)
        elif message == b'OFF':
            print('Resistencia 4 OFF')#Apagar Resistencia
            R4_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'temperatura/control/5':#Resistencia 5
        if message == b'ON':
            print('Resistencia 5 ON')#Encender Resistencia
            R5_pin.value(1)
        elif message == b'OFF':
            print('Resistencia 5 OFF')#Apagar Resistencia
            R5_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/1':#motor 1
        if message == b'ON':
            print('motor 1 ON')#Encender motor
            M1_pin.value(1)
        elif message == b'OFF':
            print('motor 1 OFF')#Apagar motor
            M1_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/2':#motor 2
        if message == b'ON':
            print('motor 2 ON')#Encender motor
            M2_pin.value(1)
        elif message == b'OFF':
            print('motor 2 OFF')#Apagar motor
            M2_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/3':#motor 3
        if message == b'ON':
            print('motor 3 ON')#Encender motor
            M3_pin.value(1)
        elif message == b'OFF':
            print('motor 3 OFF')#Apagar motor
            M3_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/4':#motor 4
        if message == b'ON':
            print('motor 4 ON')#Encender motor
            M4_pin.value(1)
        elif message == b'OFF':
            print('motor 4 OFF')#Apagar motor
            M4_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/5':#motor 5
        if message == b'ON':
            print('motor 5 ON')#Encender motor
            M5_pin.value(1)
        elif message == b'OFF':
            print('motor 5 OFF')#Apagar motor
            M5_pin.value(0)
        else:
            print('Comando sin Reconocer')
    elif topic == b'motores/control/reb':#motor 5
        if message == b'ON':
            print('motor reb ON')#Encender motor
            reb_pin.duty_u16(30000)
        elif message == b'OFF':
            print('motor reb OFF')#Apagar motor
            reb_pin.duty_u16(0)
        else:
            print('Comando sin Reconocer')        
    else:
        print('Topic sin Reconocer')
try:
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error de Conexion con Red Wi-Fi...')
    else:
        #Conectamos con MQTT Broker, iniciamos MQTT Client y nos subscribimos al Topic
        client = connect_mqtt()
        client.set_callback(my_callback)
        for rom in range(len(MQTT_TOPIC_SUB_RESISTENCIAS)):
            subscribe(client, MQTT_TOPIC_SUB_RESISTENCIAS[rom])
            time.sleep(0.2)
        while True:
            #Activamos el sensor para lectura de Temperatura 
            ds_sensor.convert_temp()
            time.sleep_ms(750)
            #Leemos la temperatura e imprimimos su valor de cada sensor y direccion
            for rom in range(number_devices):
                tempC = ds_sensor.read_temp(roms[rom])
                print("Sensor N° {}, Temperatura = {:.2f}".format(rom+1, tempC))
                print()
                #Publicamos el mensaje por MQTT
                publish_mqtt(MQTT_TOPIC_PUB_TEMPERATURE[rom], str(tempC))
                time.sleep(0.5)
                client.check_msg()
            print('Temperaturas Publicadas')                
            time.sleep(3)
            
except Exception as e:
    print('Error:', e)
    reb_pin.deinit()