# Manual Técnico para el desarrollador

La aplicación está desarrollada siguiendo una arquitectura modular, por lo que cada "componente" de la aplicación está separado como un módulo con el objetivo de organizar el desarrollo y funcionalidad de cada elemento de la aplicación.


## Estructura del proyecto

Estructura general del proyecto:

```
gps-product-forecast/
├── README.md
├── app
├── assets
├── env
├── model-ml
├── python-scripts
└── requirements.txt
```


La aplicación se compone de los siguientes elementos:

#### Utilidades:

```
model-ml/
├── demand-forecast-python.py
├── model.pkl
└── model.py
```

#### Assets (recursos):

```
assets/
├── dataset
│   ├── base-historical-product-demand.csv
│   ├── historical-product-demand.csv
│   └── test-historical-product-demand.csv
└── images
    ├── demanda-grupo-almacen.png
    ├── demanda-producto-ala.png
    ├── demanda-producto-alc.png
    ├── demanda-producto-alj.png
    ├── demanda-producto-als.png
    ├── demanda-producto-cat19.png
    ├── demanda-tiempo-general.png
    └── placeholder.txt
```

#### env 

```
env/
├── bin
├── include
├── lib
├── lib64 -> lib
├── pyvenv.cfg
└── share
```

#### Apliación

```
app/
├── assets
│   ├── datasets
│   └── images
├── client
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   └── src
└── server
    ├── model.pkl
    └── server.py
```

## Ejecución del proyecto

Los principales componentes del proyecto son el cliente y el servidor, para ejecutar cada uno de estos
componentes ejecutamos lo siguiente:

### Inicio y compilación del cliente:

Para iniciar el cliente de nuestra aplicación y compilar nuestros componentes escrito en React ⚛️

```
# ./app/client

$ npm install
$ npm run start
```


### Inicio del servidor:

Para iniciar el servidor escrito en Flask 🌶️ se debe de ejecutar:

```
# ./app/server/

$ source env/bin/activate
(env) $ python3 server.py 
```

### Entranmiento del modelo

El modelo de machine learning utilizado para las predicciones de demanda del producto en función al número
de días.

**Instalación de requerimientos**

Ejecutar el comando de instalación de requerimientos

```
# ./

pip install -r requiriments.txt

# Iniciar el entorno virtual

$ source env/bin/activate
(env) $ python3 model.py
```

Una vez teniendo todo preparado y haber instalado dependencias e iniciado enternos virtuales, se está listo para desarrollar.