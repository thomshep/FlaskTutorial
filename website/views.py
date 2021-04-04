from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

#en este archivo definiremos las rutas que tendra nuestra aplicacion, Blueprint nos permite hacer esto
#la ruta que nos permite autenicarnos esta en auth.py, el resto de rutas estan aca
views = Blueprint('views', __name__)

#ahora definiremos rutas. 
# views.route('/rutaparaacceder') nos decora la funcion de abajo diciendo que lo que devuelva la funcion (sera un HTML) se podra acceder cuando la ruta sea la indicada
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    #metodo post para ingresar nueva nota
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    #retornamos el template home.html renderizado usando la funcion render_template que importamos de flask. current_user lo importamos, nos guarda quien esta logueado si es que hay alguien
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    #tomamos lo que se nos mando (un JSON con el id de la nota a borrar, esto nos lo manda la funcion definida en el archivo javascript)
    note = json.loads(request.data)
    noteId = note['noteId']
    #buscamos la nota en la base de datos con ese id
    note = Note.query.get(noteId)
    #si hay alguna nota con ese id
    if note:
        #si la nota pertenece al usuario que esta en la sesion
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
