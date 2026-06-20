from flask import Blueprint, render_template, flash, redirect, url_for, request
from ..models.curso import Curso
from ..extension import db


curso_bp = Blueprint('curso', __name__)

@curso_bp.route("/cursos", methods=['GET'])
def cursos():

    cursos = Curso.query.all()
    
    return render_template("cursos/listar.html", cursos=cursos)

    
    
