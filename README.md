# Sistema de descuento Meli y Web

Automatización para el descuento de productos vendidos en mercado libre y pagina web (Proximamente canjes)

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Prerrequisitos 📋

1.- Instalar python desde la pagina oficial:

- [Descarga de python](https://www.python.org/downloads/)

2.- Verificar instalacion de python

```bash
  python --version
```

3.- Verificar la instalación del gestor de paquetes PIP

```bash
  pip --version
```

4.- Instalación de editor de codigo Visual Studio Code 

- [Descarga de VSC](https://code.visualstudio.com/)


## Instalación local

Abrir visual estudio code y abrir una terminal con Ctrl+Shift+ñ

hacer un clon del repositorio

```bash
  git clone https://github.com/kniball4726/Python.git
```

Desde el terminal entrar en la carpeta Python

```bash
  cd python
```

Estando dentro del proyecto desde terminal se debe crear un entorno virtual

```bash
  python -m venv .venv
```

Para activar el entorno virtual se debe entrar en la carpeta .venv/Scrips y correr Activate de la siguiente manera 

```bash
  cd .\.venv\Scripts\
```
```bash
  .\activate
```
Volvemos a la carpeta raiz de nuestro proyecto 

```bash
  cd ../..
```
Se deben instalar las dependencias utilizadas en el proyecto para que funciona de manera optima

```bash
  pip install -r requirements.txt
```

para hacer un despliegue con ejecutable desde windows se debe usar:

```bash
    pyinstaller --onefile app.py
```

al correr este comando se crearan dos carpetas denominadas `build` y `dist`

dentro de la carpeta `dist` encontraremos un archivo llamado `main.exe`

este ejecutable de windows puede utilizarse directamente desde el escritorio de su pc otorgandole un acceso directo, se puede modificar el nombre y el icono

## Forma de uso

- Al ejecutar el programa le va a solicitar el valor de a o coeficiente cuadratico dentro de la función f(x)=ax^2+bx+c
- es el valor de ax^2
- El valor de b seria el valor de bx o el coeficiente lineal
- El valor de c seria el coeficiente independiente
- Al introducir estos valores el sistema calcula toda la información que genera la funcion cuadratica como lo son los vertices, las raices, rango, dominio, concavidad, el eje de simetria, entre otras
- Asi como tambien genra el grafico de dicha Función cuadratica.
   
## Documentación

En la carpeta raiz se encuentra un archivo llamado `documentacion.py` al ejecutar este archivo por terminal se observa la documentación completa de todas las funciones utilizadas en la aplicación

## Autor

Gregory Rodriguez - Trabajo inicial, Desarrollo y documentación
