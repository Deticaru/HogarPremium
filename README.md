# Instrucciones para ejecutar el proyecto en Windows

Este documento explica cómo crear y activar un entorno virtual (`.venv`), instalar las dependencias y arrancar el proyecto Django en Windows (PowerShell o CMD).

Requisitos previos
- Tener instalado Python 3.8+ y que `python` o `py` esté disponible en el `PATH`.
- Archivo `requirements.txt` en la raíz del proyecto (ya incluido en este repo).

Pasos (PowerShell recomendado)

1. Abrir PowerShell en la carpeta raíz del proyecto (donde está `manage.py`).

2. Crear el entorno virtual `.venv`:

```powershell
python -m venv .venv
# O si usas el lanzador de Windows:
py -3 -m venv .venv
```

3. Activar el entorno virtual (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts, ejecuta (una sola vez) como administrador o en tu sesión:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

Alternativa (CMD):

```cmd
.venv\Scripts\activate.bat
```

4. Actualizar `pip` e instalar requerimientos:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

5. Iniciar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Fin
