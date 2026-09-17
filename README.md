# Catálogo de Juegos

Proyecto Django para un catálogo de juegos con páginas de inicio y detalle.

## Requisitos

- Python 3.10 o superior
- pip
- Git

## 1. Clonar el repositorio

```bash
git clone https://github.com/Gonzal0Munoz80/Sumativa1-backend.git
cd Sumativa1-backend
```

## 2. Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

## 3. Instalar dependencias

Si existe un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si no existe, instala Django manualmente:

```bash
pip install django
```

## 4. Ejecutar migraciones

```bash
python manage.py migrate
```

## 5. Iniciar el servidor

```bash
python manage.py runserver
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/inicio/
```

## 6. Rutas principales

- Inicio: `http://127.0.0.1:8000/inicio/`
- Detalle: `http://127.0.0.1:8000/detalle/<id>/`

Ejemplo:

```text
http://127.0.0.1:8000/detalle/1/
```

## 7. Estructura básica

```text
config/
static/
templates/
inicio/
detalle/
manage.py
README.md
```

## 8. Deteener el servidor

Presiona:

```text
CTRL + C
```
