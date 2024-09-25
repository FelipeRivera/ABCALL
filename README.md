# Proyecto de Arquitectura: Seguridad

## Descripción
Este proyecto es un experimento diseñado para probar estrategias de separación de entidades, identificación, autenticación y autorización de actores, utilizando Docker y Nginx.

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

### 5. Probar los servicios

Una vez que los contenedores estén en ejecución, puedes probar los servicios utilizando herramientas como **Postman** o **cURL**. A continuación se detallan algunos endpoints importantes:

#### 1. Obtener token de autorización

Para autenticarte y obtener un token de acceso, realiza una solicitud `POST` al siguiente endpoint:

- **Método HTTP**: `POST`
- **URL**: `http://localhost:8881/public/auth/login`
  
Credenciales de acceso:

- **Administrador**:
  - **Usuario**: `admin`
  - **Contraseña**: `123456`
  
- **Invitado**:
  - **Usuario**: `gues`
  - **Contraseña**: `123456`

El token de acceso devuelto deberá ser utilizado en las siguientes solicitudes a las APIs públicas y privadas.

#### 2. Acceder a la API pública

Esta API está disponible tanto para administradores como para invitados. El token de acceso obtenido debe enviarse como parte de la solicitud.

- **Método HTTP**: `GET`
- **URL**: `http://localhost:8881/public/product/all`
- **Nota**: Incluye el token de acceso en los encabezados de la solicitud.

#### 3. Acceder a la API privada (Solo para administradores)

Esta API es accesible únicamente por administradores. Asegúrate de enviar el token de acceso correspondiente al usuario administrador.

- **Método HTTP**: `GET`
- **URL**: `http://localhost:8881/protected/product/9`
- **Nota**: El token de acceso de administrador es necesario para acceder a este endpoint.

---