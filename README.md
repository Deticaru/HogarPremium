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

5. Aplicar migraciones de la base de datos:

```powershell
python manage.py migrate
```

6. (Opcional) Crear superusuario para el admin:

```powershell
python manage.py createsuperuser
```

7. Iniciar el servidor de desarrollo:

```powershell
python manage.py runserver
```

8. Detener y desactivar el entorno virtual:

```powershell
deactivate
```

Notas útiles
- Si `python` no está disponible en `PATH`, usa `py -3` en lugar de `python`.
- Para eliminar el entorno virtual en PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
```

Fin

Si quieres, puedo añadir instrucciones específicas para entornos como Git Bash o para desplegar estático (`collectstatic`).
