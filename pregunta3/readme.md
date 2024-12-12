# Pregunta 3: Manejador de tablas virtuales

#### Nombre: Néstor Herrera
#### Carnet: 18-10796

Para ejecutar el programa, usar el comando `python -u vTables.py`. Se le pediran al usuario las instrucciones segun el enunciado.

## Contenidos de los archivos

**vTables.py**
- Se maneja el input del usuario y se decide que funciones ejecutar

**funciones.py**
- Logica del programa con las diferentes opciones.
- Estructuras para guardar los datos

El resto de los archivos se describen a continuación

## Tests

Para los test y cobertura se utilizan `pytest` y `coverage`. El informe devuelve una cobertura del 97% en total, con una cobertura de 95% para `funciones.py`.

En el archivo `index.html` pueden encontrarse la cobertura de las pruebas realizadas en el archivo `test_funciones.py`

Tambien pueden ejecutarse las pruebas usando `pytest` y generar el reporte usando `coverage run -m pytest`. Se muestra este reporte en el terminal al usar `coverage report`, y se genera el archivo html mencionado al usar `coverage html`.