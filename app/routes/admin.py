from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from ..models.curso import Curso
from ..extension import db
import os


admin_bp = Blueprint("admin", __name__)



@admin_bp.route("/admin/dashboard", methods=["GET"])
def dashboard():
    return render_template("admin/dashboard.html")





@admin_bp.route("/admin/cursos", methods=['GET'])
def cursos():

    cursos = Curso.query.all()
    
    return render_template("admin/listar_cursos.html", cursos=cursos)


@admin_bp.route("/admin/nuevos", methods=["GET", "POST"])
def crear_curso():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        imagen = request.files.get("imagen")

        ruta_imagen = "img/cursos/default.jpg"

        if imagen and imagen.filename:

            nombre_archivo = secure_filename(imagen.filename)

            ruta_carpeta = os.path.join(
                current_app.root_path,
                "static",
                "img",
                "cursos"
            )

            os.makedirs(ruta_carpeta, exist_ok=True)

            ruta_archivo = os.path.join(
                ruta_carpeta,
                nombre_archivo
            )

            imagen.save(ruta_archivo)

            ruta_imagen = f"img/cursos/{nombre_archivo}"

        data = Curso(
            nombre=nombre,
            descripcion=descripcion,
            imagen=ruta_imagen
        )

        try:

            db.session.add(data)
            db.session.commit()

            flash("Curso creado con éxito", "success")

            return redirect(
                url_for("admin.cursos")
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error al guardar el curso: {e}",
                "danger"
            )

            return redirect(
                url_for("admin.crear_curso")
            )

    return render_template(
        "admin/crear_curso.html"
    )




@admin_bp.route("/admin/editar/<int:id>", methods=["GET","POST"])
def editar_curso(id):
     
    curso = Curso.query.get_or_404(id)
        
    if request.method == "POST":

        curso.nombre = request.form.get("nombre")
        curso.descripcion = request.form.get("descripcion")
        imagen = request.files.get("imagen")
        print("FORM:", request.form)
        print("FILES:", request.files)
        print("IMAGEN:", imagen)

        

        if imagen and imagen.filename:
            print(imagen)
            print(imagen.filename if imagen else "SIN IMAGEN")
            nombre_archivo =secure_filename(imagen.filename)

            ruta_carpeta = os.path.join(
                current_app.root_path,
                "static",
                "img",
                "cursos"
            )

            os.makedirs(ruta_carpeta, exist_ok=True)

            ruta_archivo = os.path.join(
                ruta_carpeta,
                nombre_archivo
            )

            imagen.save(ruta_archivo)
            print(ruta_archivo)

            curso.imagen = f"img/cursos/{nombre_archivo}"


        try:

            db.session.commit()
            flash("Curso actualizado exitosamente", "success")
            return redirect(url_for("admin.cursos")) 

        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar  el curso: {e}', "danger")
            return redirect(url_for('admin.cursos'))
    
    return render_template("admin/editar_curso.html", curso=curso)



@admin_bp.route("/admin/eliminar/<int:id>", methods=["POST"])
def eliminar_curso(id):

    curso = Curso.query.get_or_404(id)

    try:
        
        db.session.delete(curso)
        db.session.commit()
        flash("Curso eliminado exitosamente", "success")
        return redirect(url_for("admin.cursos")) 
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar el curso: {e}', "danger")
        return redirect(url_for('admin.cursos'))