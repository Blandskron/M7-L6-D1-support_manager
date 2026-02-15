## Paso a paso para crear el proyecto

1. Crear entorno virtual

```bash
python -m venv venv
```

2. Activar entorno virtual (Windows)

```bash
venv\Scripts\activate
```

3. Actualizar pip

```bash
python -m pip install --upgrade pip
```

4. Instalar Django

```bash
pip install django
```

5. Crear proyecto

```bash
django-admin startproject support_manager
```

6. Entrar a la carpeta del proyecto

```bash
cd support_manager
```

7. Crear aplicación

```bash
python manage.py startapp clients
```

8. Registrar la app en `support_manager/settings.py`

```python
INSTALLED_APPS = [
    ...
    'clients',
]
```

9. Incluir rutas de la app en `support_manager/urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('', include('clients.urls')),
]
```

10. Crear/editar archivos esenciales dentro de `clients/`

* `clients/models.py`
* `clients/forms.py`
* `clients/views.py`
* `clients/urls.py`

11. Crear templates dentro de `clients/templates/clients/`

* `base.html`
* `client_list.html`
* `client_form.html`
* `client_confirm_delete.html`
* `ticket_list.html`
* `ticket_form.html`
* `ticket_confirm_delete.html`

12. Crear migraciones

```bash
python manage.py makemigrations
```

13. Aplicar migraciones

```bash
python manage.py migrate
```

14. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

15. Ejecutar servidor

```bash
python manage.py runserver
```

16. Abrir en navegador

* `http://127.0.0.1:8000/clients/`
* `http://127.0.0.1:8000/tickets/`
