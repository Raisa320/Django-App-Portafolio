
# Project Django Portafolio

A simple blog application created using Django framework.

## Setup


### Install Python

Install Python 3.10

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Install virtualenv

Virtualenv una herramienta para crear entornos virtuales de Python. Esto es útil para aislar las dependencias de un proyecto de las dependencias de otros proyectos.

```bash
pip install virtualenv
```

### Crear una máquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la máquina virtual

```bash
source venv/bin/activate
```

- windows

```bash
venv\Scripts\activate

venv/Scripts/activate.ps1
```

### Requirements

Instalar las módulos necesarios para iniciar el proyecto
```bash
pip install -r requirements.txt
```
    
## Para la base de datos

### Migraciones en la base de datos

Run migrations with the following commands

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```
## Run Locally

Start the server

```bash
  python manage.py runserver
```
## Authors

- [Raisa Orellana](https://github.com/Raisa320)


