flask db init
flask db migrate -m "crear tabla curso"
flask db upgrade
flask db migrate



# documentacion de rutas 
pip install flask-smorest

CURSOS
------

GET     /cursos
GET     /admin/cursos
GET     /admin/nuevos
POST    /admin/nuevos
GET     /admin/editar/<id>
POST    /admin/editar/<id>
POST    /admin/eliminar/<id>

CLASES
------

GET     /curso/<curso_id>/clases
GET     /clase/nueva
POST    /clase/nueva
GET     /clase/editar/<id>
POST    /clase/editar/<id>
POST    /clase/eliminar/<id>

# ACADEMIA PYTHON - DOCUMENTACIÓN DE RUTAS

## CURSOS (PÚBLICO)

### Listar Cursos

GET /cursos

Muestra todos los cursos disponibles para los estudiantes.

## ADMINISTRACIÓN DE CURSOS

### Listar Cursos

GET /admin/cursos

Muestra todos los cursos registrados.

### Crear Curso

GET /admin/nuevos

Muestra el formulario de creación.

POST /admin/nuevos

Guarda un nuevo curso.

### Editar Curso

GET /admin/editar/<id>

Muestra el formulario de edición.

POST /admin/editar/<id>

Actualiza el curso seleccionado.

### Eliminar Curso

POST /admin/eliminar/<id>

Elimina un curso.

---

## CLASES

### Listar Clases de un Curso

GET /curso/<curso_id>/clases

Muestra todas las clases asociadas a un curso.

### Crear Clase

GET /clase/nueva

Muestra el formulario para crear una clase.

POST /clase/nueva

Guarda una nueva clase.

### Editar Clase

GET /clase/editar/<id>

Muestra el formulario de edición.

POST /clase/editar/<id>

Actualiza la clase seleccionada.

### Eliminar Clase

POST /clase/eliminar/<id>

Elimina una clase.

---

## FUTURO: UNIDADES

### Listar Unidades

GET /clase/<clase_id>/unidades

### Crear Unidad

GET /unidad/nueva

POST /unidad/nueva

### Editar Unidad

GET /unidad/editar/<id>

POST /unidad/editar/<id>

### Eliminar Unidad

POST /unidad/eliminar/<id>

---

## FUTURO: EJERCICIOS

### Listar Ejercicios

GET /unidad/<unidad_id>/ejercicios

### Crear Ejercicio

GET /ejercicio/nuevo

POST /ejercicio/nuevo

### Editar Ejercicio

GET /ejercicio/editar/<id>

POST /ejercicio/editar/<id>

### Eliminar Ejercicio

POST /ejercicio/eliminar/<id>




# DOCUMENTACIÓN DE RUTAS - ACADEMIA PYTHON

## CURSOS

### Listar Cursos

http://127.0.0.1:5000/cursos

### Panel Administrador Cursos

http://127.0.0.1:5000/admin/cursos

### Crear Curso

http://127.0.0.1:5000/admin/nuevos

### Editar Curso

http://127.0.0.1:5000/admin/editar/1

### Eliminar Curso

POST:
http://127.0.0.1:5000/admin/eliminar/1

---

## CLASES

# Listar Clases 
http://127.0.0.1:5000/clases/ver_clases

### Listar Clases de un Curso

Curso 1:
http://127.0.0.1:5000/curso/1/clases

Curso 2:
http://127.0.0.1:5000/curso/2/clases

Curso 3:
http://127.0.0.1:5000/curso/3/clases

### Crear Clase

http://127.0.0.1:5000/clase/nueva

### Editar Clase

Clase 1:
http://127.0.0.1:5000/clase/editar/1

Clase 2:
http://127.0.0.1:5000/clase/editar/2

Clase 3:
http://127.0.0.1:5000/clase/editar/3

### Eliminar Clase

POST:
http://127.0.0.1:5000/clase/eliminar/1

---

## UNIDADES (PENDIENTE)

### Listar Unidades de una Clase

http://127.0.0.1:5000/clase/1/unidades

### Crear Unidad

http://127.0.0.1:5000/unidad/nueva

### Editar Unidad

http://127.0.0.1:5000/unidad/editar/1

### Eliminar Unidad

POST:
http://127.0.0.1:5000/unidad/eliminar/1

---

## EJERCICIOS (PENDIENTE)

### Listar Ejercicios de una Unidad

http://127.0.0.1:5000/unidad/1/ejercicios

### Crear Ejercicio

http://127.0.0.1:5000/ejercicio/nuevo

### Editar Ejercicio

http://127.0.0.1:5000/ejercicio/editar/1

### Eliminar Ejercicio

POST:
http://127.0.0.1:5000/ejercicio/eliminar/1

---

## PATRÓN DEL PROYECTO

LISTAR:
/modulo

CREAR:
/modulo/nuevo

EDITAR:
/modulo/editar/<id>

ELIMINAR:
/modulo/eliminar/<id>

Ejemplos:

/curso/editar/5
/clase/editar/12
/unidad/editar/8
/ejercicio/editar/15
