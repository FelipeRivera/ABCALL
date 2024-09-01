# Proyecto de Arquitectura: Votación y Redundancia Activa

## Descripción
Este es un experimento para probar tácticas de arquitectura de votación y redundancia activa, realizado utilizando Docker y Nginx.

## Pasos para correr el proyecto

### 1. Asegúrese de tener Docker instalado en su máquina
Docker es una plataforma que permite automatizar la implementación de aplicaciones en contenedores. Si aún no lo tiene instalado, puede seguir las instrucciones en [la página oficial de Docker](https://docs.docker.com/get-docker/).

### 2. Verifique que Docker esté corriendo
Una vez que Docker esté instalado, asegúrese de que el servicio esté en ejecución. Si Docker no está corriendo, obtendrá un error indicando que no se puede encontrar el daemon de Docker.

### 3. Ejecute el comando de build
docker compose build

Este comando construye las imágenes Docker especificadas en el archivo docker-compose.yml. Si alguna de las imágenes ya existe, se utilizará la caché, lo que puede acelerar el proceso.

### 4. Inicie los servicios
docker compose up -d --force-recreate

Este comando levanta todos los servicios definidos en docker-compose.yml en segundo plano (-d). La opción --force-recreate asegura que los contenedores se vuelvan a crear, incluso si no hay cambios en la configuración o el código.

### 5. Pruebe el servicio
Una vez que los contenedores estén corriendo, puede probar el servicio utilizando Postman u otra herramienta de API. Realice una petición GET a la siguiente URL:
http://localhost:8881/public/product/all

Esto le permitirá acceder al servicio y verificar que está funcionando correctamente.
