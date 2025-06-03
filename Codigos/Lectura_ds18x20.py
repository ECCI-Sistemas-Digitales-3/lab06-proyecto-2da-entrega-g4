# - machine: permite acceder a pines y hardware del microcontrolador.
# - time: para realizar pausas y temporizaciones.
# - onewire: protocolo de comunicación para sensores DS18B20.
# - ds18x20: librería específica para controlar sensores DS18B20.
import machine, time, onewire, ds18x20

# Declaramos el pin GPIO 22 como pin de datos del sensor.
# Aquí conectamos la línea de datos del sensor DS18B20.
ds_pin = machine.Pin(22)

# Inicializamos el bus OneWire sobre el pin seleccionado.
# Esto permite comunicarnos con uno o varios sensores DS18B20 usando un solo cable de datos.
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Escaneamos el bus OneWire para detectar todos los sensores conectados.
# Cada sensor tiene una dirección única (ROM) que se guarda en la lista 'roms'.
roms = ds_sensor.scan()

# Contamos cuántos sensores fueron detectados.
number_devices = len(roms)

# Mostramos por consola cuántos sensores fueron encontrados y sus direcciones únicas.
print('Numero de sensores= ', number_devices)
print('Direccion= ', roms)

# Bucle infinito para realizar lecturas periódicas de temperatura.
while True:
    # Enviamos la orden a los sensores para que realicen la conversión de temperatura.
    # Esto toma un tiempo, por lo que se recomienda esperar al menos 750 milisegundos.
    ds_sensor.convert_temp()
    time.sleep_ms(750)

    # Recorremos la lista de sensores detectados (por su dirección ROM)
    for rom in roms:
        # Leemos la temperatura en grados Celsius desde el sensor actual.
        tempC = ds_sensor.read_temp(rom)

        # Imprimimos la dirección del sensor (para identificar cuál es cuál)
        print(rom)

        # Imprimimos la temperatura leída con dos decimales de precisión.
        print('temperature (ºC):', "{:.2f}".format(tempC))
        print()  # Línea en blanco para separar lecturas

    # Esperamos 5 segundos antes de hacer otra lectura.
    time.sleep(5)
