from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from ..models.clase import Clase
from ..models.curso import Curso
from ..extension import db
import os


clase_bp = Blueprint("clase", __name__)

@clase_bp.route("/clases/ver_clases", methods=["GET"])
def ver_clases():
    clases = Clase.query.all()

    return render_template("clases/clases.html", clases=clases)



@clase_bp.route("/curso/<int:curso_id>/clases", methods=["GET"])
def listar_clase(curso_id):
    clases = Clase.query.filter_by(curso_id=curso_id).all()

    return render_template("clases/listar_clases.html", clases=clases)


@clase_bp.route("/clase/nueva", methods=["GET"])
def clase_nueva():
    cursos = Curso.query.all()

    return render_template("clases/crear_clase.html", cursos=cursos)


@clase_bp.route("/clase/nueva", methods=["GET", "POST"])
def crear_clase():

    if request.method == "POST":

        titulo = request.form.get("titulo")
        contenido = request.form.get("contenido")
        orden = request.form.get("orden")
        imagen = request.files.get("imagen")
        video = request.files.get("video")
        curso_id = request.form.get("curso_id")

        ruta_imagen = "img/clases/default.jpg"
        ruta_video = "img/videos/default.jpg"

        if imagen and imagen.filename:
            nombre_archivo = secure_filename(imagen.filename)
            ruta_carpeta = os.path.join(
                current_app.root_path,
                "static",
                'img',
                'clases'
            )

            os.makedirs(ruta_carpeta, exist_ok=True)
            ruta_archivo_imagen = os.path.join(ruta_carpeta, nombre_archivo)

            imagen.save(ruta_archivo_imagen)
            ruta_imagen = f"img/clases/{nombre_archivo}"

        
        if video and video.filename:
            archivo = secure_filename(video.filename)
            ruta_carpeta = os.path.join(
                current_app.root_path,
                "static",
                'videos',
                'clases'
            )

            os.makedirs(ruta_carpeta, exist_ok=True)
            ruta_archivo_video = os.path.join(ruta_carpeta, archivo)

            video.save(ruta_archivo_video)
            ruta_video = f"videos/clases/{archivo}"


        data = Clase(
            titulo=titulo,
            contenido=contenido,
            orden=orden,
            imagen=ruta_imagen,
            video=ruta_video,
            curso_id=curso_id
        )

        try:

            db.session.add(data)
            db.session.commit()
            flash("Clase creada con exito")
            return redirect(url_for("clase.listar_clase", curso_id=curso_id))
        
            cursos = Curso.query.all()

            return render_template(
                "clases/crear_clase.html",
                cursos=cursos
            )

        except Exception as e:

            db.session.rollback()
            print("ERROR:", e)

            flash(
                f"Error al crear la clase: {e}",
                "danger"
            )

            cursos = Curso.query.all()

            return render_template(
                "clases/crear_clase.html",
                cursos=cursos
            )



@clase_bp.route("/clase/editar", methods=["GET"])
def formulario_editar():

    return render_template("editar_clase.html")




@clase_bp.route("/clase/editar/<int:id>", methods=["GET","POST"])
def editar_clase(id):

    clase = Clase.query.get_or_404(id)

    if request.method == "POST":

        clase.titulo = request.form.get("titulo")
        clase.contenido = request.form.get("contenido")
        clase.orden = request.form.get("orden")
        clase.curso_id = request.form.get("curso_id")

        imagen = request.files.get("imagen")

        if imagen and imagen.filename:
            # guardar imagen
            pass

        video = request.files.get("video")

        if video and video.filename:
            # guardar video
            pass

        try:

            db.session.commit()

            flash(
                "Clase actualizada exitosamente",
                "success"
            )

            return redirect(
                url_for(
                    "clase.listar_clase",
                    curso_id=clase.curso_id
                )
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error al actualizar la clase: {e}",
                "danger"
            )

    cursos = Curso.query.all()

    return render_template(
        "clases/editar_clase.html",
        clase=clase,
        cursos=cursos
    )


@clase_bp.route("/clase/eliminar/<int:id>", methods=["GET","POST"])
def eliminar_clase(id):
    clase = Clase.query.get_or_404(id)

    db.session.delete(clase)
    db.session.commit()
    flash("Clase eliminada")

    return redirect(url_for("clase.ver_clases"))

    
