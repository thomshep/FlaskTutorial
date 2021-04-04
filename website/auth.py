from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
#nunca se guarda la contrasena en texto plano, esto me ayudara a asegurar las contrasenas en la base de datos. funcion de hash -> no tiene inversa, ideal para guardar contrasena
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#esto nos ayuda muchisimo para saber si hay usuario logueado, quien es, etc.
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

#defino ruta login que puede aceptar metodos post y get (por defecto acepta GET). El metodo GET se usa al acceder a la ruta (pedimos el HTML de la pagina), el metodo POST se usa al darle al boton Submit (estamos queriendo crear un usuario nuevo). Recordar que el form del HTML tiene method="POST".
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #request se importo de flask
    #si el metodo request es post, entonces se envio el formulario
    if request.method == 'POST':
        #obtengo la info que se mando en el formulario. Puedo usar 'email' y 'password' porque tengo cosas en el formulario con ese name (importa el name en esto y no el id)
        email = request.form.get('email')
        password = request.form.get('password')

        #hacemos consulta a la base de datos para buscar por email (por si acaso hay varios, pedimos el primero)
        user = User.query.filter_by(email=email).first()
        if user:
            #chequeamos que la contrasena es correcta
            if check_password_hash(user.password, password):
                #flash lo importamos de flask, sirve para devolverle un mensaje al frontend. La categoria la puedo inventar, es para tener una idea de que paso
                flash('Logged in successfully!', category='success')
                #registramos que user inicio sesion y hacemos que lo recuerde
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

#el decorator login_required nos asegura que no se va a poder acceder a esta pagina si no hay nadie logueado
@auth.route('/logout')
@login_required
def logout():
    #registramos que el usuario se salio
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #creo usuario, lo agrego, y hago commit de eso para que quede guardado
            # sha256 es un algoritmo de hash para generar la contrasena encriptada
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            #los redireccionaremos al home
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
