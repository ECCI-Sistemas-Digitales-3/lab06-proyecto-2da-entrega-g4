[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19556764&assignment_repo_type=AssignmentRepo)

# Lab06: Proyecto 2da Entrega - Control de Temperatura para Mezclador de Pinturas

## 📘 Descripción general

Esta entrega contiene la segunda entrega del proyecto integrador para el laboratorio 06 del curso Sistemas Digitales 3 en la Universidad ECCI. El proyecto se centra en la implementación de un sistema de control de temperatura para un **Mezclador de Pinturas**, utilizando tecnologías embebidas.

El sistema está basado en **Micropython**, un lenguaje derivado de Python diseñado para microcontroladores y dispositivos con recursos limitados. Debido a las diferencias con Python convencional, gran parte del código incluye librerías adaptadas para el entorno Micropython, en particular para manejar comunicación MQTT.

---

## 📂 Estructura del repositorio

- [`Codigos/`](https://github.com/ECCI-Sistemas-Digitales-3/lab06-proyecto-2da-entrega-g4/tree/main/Codigos)
 Contiene los códigos fuente en **Micropython** que implementan la lógica del control de temperatura y comunicación MQTT para el mezclador de pinturas.

- [`Imagenes/`]()  
  Diagramas, capturas y recursos visuales relacionados con el proyecto.

- `.github/`  
  Configuraciones y workflows para GitHub Actions.

- `flows.json`  
  Archivo de configuración para simulaciones o flujos relacionados.

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


