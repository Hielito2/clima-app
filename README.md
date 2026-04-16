Aplicación de línea de comandos escrita en Python que obtiene el clima actual y pronóstico de cualquier ciudad del mundo utilizando la API de OpenWeatherMap.

Utiliza el **código de ciudad** (*city code*), el que sale en la url en OpenWeatherMap al buscar la ciudad.

## Características

- Clima actual: temperatura, sensación térmica, presión, humedad, visibilidad y descripción meteorológica.
- Pronóstico extendido (hasta 5 días, con datos cada 3 horas).
- Modo **verbose** (`-v`) para medir el tiempo de respuesta de la API (útil para depuración y medición de rendimiento).
- Manejo de zona horaria local automático.

---

## Requisitos

- Python 3.6 o superior.
- Biblioteca `requests` (instalable vía pip).
- Conexión a Internet.

---

## Instalación y configuración

1. **Clonar el repositorio:**
   ```bash
   https://github.com/Hielito2/clima-app.git
   cd clima-app
   ```
2. Obtener API en https://openweathermap.org/ y renombra el archivo de example-config.py -> config.py y poner la API adentro
3. Podrias usar la API que usa openweathermap, con el web developer tool en una los XHR las url tienen una API, puedes usar esa.
