import machine, time, onewire, ds18x20

#Declaramos el pin que usaremos para la lectura
ds_pin = machine.Pin(22)
#Definimos la comunicacion por un solo cable
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
#Guardamos las direcciones de los sensores DS18B20
roms = ds_sensor.scan()
#Declaramos cuantos sensores tenemos
number_devices = len(roms)
#roms = [b'\x28\xd7\x6a\x84\x00\x00\x00\x24']

#Imprimimos la cantidad de sensores y sus direcciones
print('Numero de sensores= ', number_devices)
print('Direccion= ', roms)

while True:
    #Activamos el sensor para lectura de Temperatura 
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    #Leemos la temperatura e imprimimos su valor de cada sensor y direccion
    for rom in roms:
        tempC = ds_sensor.read_temp(rom)
        print(rom)
        print('temperature (ºC):', "{:.2f}".format(tempC))
        print()
    time.sleep(5)