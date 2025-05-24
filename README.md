[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19556764&assignment_repo_type=AssignmentRepo)

# Lab06: Proyecto 2da Entrega - Control de Temperatura para Mezclador de Pinturas

## 📘 Descripción general

Esta entrega contiene la segunda entrega del proyecto integrador para el laboratorio 06 del curso Sistemas Digitales 3 en la Universidad ECCI. El proyecto se centra en la implementación de un sistema de control de temperatura para un **Mezclador de Pinturas**, utilizando tecnologías embebidas.

El sistema está basado en **Micropython**, un lenguaje derivado de Python diseñado para microcontroladores y dispositivos con recursos limitados. Debido a las diferencias con Python convencional, gran parte del código incluye librerías adaptadas para el entorno Micropython, en particular para manejar comunicación MQTT.

---

## 📂 Estructura del repositorio

- [`Codigos/`](https://github.com/ECCI-Sistemas-Digitales-3/lab06-proyecto-2da-entrega-g4/tree/main/Codigos) Contiene los códigos fuente en **Micropython** que implementan la lógica del control de temperatura y comunicación MQTT para el mezclador de pinturas.

- [`Imagenes/`](https://github.com/ECCI-Sistemas-Digitales-3/lab06-proyecto-2da-entrega-g4/tree/main/Imagenes) Diagramas, capturas y recursos visuales relacionados con el proyecto.

- [`flows.json`](https://github.com/ECCI-Sistemas-Digitales-3/lab06-proyecto-2da-entrega-g4/blob/main/flows.json) Archivo de configuración para simulaciones o flujos relacionados.

---

## 🔧 Descripción técnica y códigos principales

### Uso de Micropython y librerías MQTT personalizadas

Micropython no incluye algunas librerías de Python estándar, por lo que fue necesario crear implementaciones propias o adaptadas para funciones clave, en especial para la comunicación MQTT, que es esencial para la telemetría y control remoto del sistema.

#### `simple.py`

- Implementa una versión básica del cliente MQTT para Micropython, basada en [micropython-lib/umqtt.simple](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.simple).
- Contiene la lógica fundamental para conectar, publicar, suscribirse y recibir mensajes MQTT.
- Funciona con sockets básicos y maneja el protocolo MQTT en un entorno ligero.

#### `robust.py`

- Extiende la funcionalidad de `simple.py` para agregar robustez en la conexión MQTT.
- Implementa reconexiones automáticas y manejo de errores recurrentes en conexiones inestables, típico en redes IoT.
- Basado en [micropython-lib/umqtt.robust](https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt.robust), con adaptaciones para este proyecto.
  
Estas librerías permiten que el dispositivo embebido mantenga comunicación confiable con el broker MQTT, facilitando el monitoreo y control remoto del sistema de temperatura del mezclador.

---

### Detalle adicional sobre uso y funcionalidad

Este proyecto utiliza MicroPython para controlar y monitorear sensores de temperatura DS18B20 en un sistema embebido, con comunicación vía MQTT para telemetría y control remoto.

El proyecto requiere adaptar librerías MQTT ligeras y personalizadas para el entorno restringido del microcontrolador, dado que MicroPython no incluye todas las librerías estándar de Python. Esto permite una comunicación confiable con un broker MQTT, fundamental para el monitoreo en tiempo real y el control remoto del sistema.

**Descripción de Scripts**

- `Lectura_ds18x20.py`  
  Gestiona la lectura de uno o varios sensores DS18B20 conectados a un pin específico, mostrando las temperaturas en consola.

- `Pub&Sub_Mqtt_ds18x20.py`  
  Combina la lectura de sensores con la publicación periódica de sus temperaturas a tópicos MQTT específicos. Además, se suscribe a tópicos de control para activar o desactivar resistencias eléctricas en el sistema, gestionando los mensajes recibidos.

- `Pub_Mqtt.py`  
  Ejemplo básico de publicación periódica de datos a un tópico MQTT, simula el envío de valores de temperatura.

- `Sub_Mqtt.py`  
  Se suscribe a un tópico MQTT y controla un LED físico en función de los mensajes recibidos (encender o apagar).

- `config.py`  
  Contiene la configuración de red Wi-Fi para facilitar la conexión de los dispositivos embebidos.

**Funcionamiento General**

Los dispositivos embebidos corren MicroPython y usan estas librerías para:

- Conectarse a una red Wi-Fi.
- Conectar y mantener sesión con un broker MQTT.
- Leer sensores de temperatura y publicar sus datos.
- Recibir comandos para controlar actuadores (resistencias, LED).
- Ejecutar acciones según comandos recibidos vía MQTT.

Este esquema facilita la creación de un sistema distribuido de monitoreo y control remoto, adaptable a distintas aplicaciones industriales o domóticas.

---

## 🛠️ Funcionalidad del sistema de control de temperatura

El código de control implementa:

- Lectura de sensores de temperatura en tiempo real.
- Publicación de datos al broker MQTT usando las librerías robustas.
- Recepción de comandos para ajustar parámetros de mezcla o alarmas.
- Reconexión automática en caso de pérdida de conexión.

Esto forma parte del proyecto integrador donde el mezclador de pinturas requiere un control preciso de temperatura para asegurar la calidad del producto final.

---

## 👥 Integrantes

| Integrantes                   |
|------------------------------|
| [`Diego Lopez`][Alejo]        |
| [`Daniel Ramirez`][Daniel]    |
| [`Sebastian Martinez`][Sebas] |

---

## 📄 Documentación adicional

Se recomienda revisar:

- Informe detallado del proyecto (en desarrollo)  
- Guía de instalación y despliegue en hardware embebido (próximamente)

---

## 👨‍🔧 Créditos

**Grupo 4 - UNIVERSIDAD ECCI**

[//]: # (Referencias)

[Alejo]: <https://github.com/Alejibiris>  
[Daniel]: <https://github.com/D4N1EL-R4M1R3Z>  
[Sebas]: <https://github.com/SebasMtz30>  


