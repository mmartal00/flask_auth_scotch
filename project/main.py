# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.name)

@main.route('/inicio')
@login_required
def inicio():
    return render_template('profile.html', name=current_user.name)


# Agregar tablero al inicio
@main.route('/tablero')
@login_required
def tablero():
    return render_template('principal.html', tipoUsuario=1)
    else:
    print (2)
    return render_template('principal.html', tipoUsuario=2)
    # return render_template('principal.html', name=current_user.name, tipoUsuario=tipoUsuario)

# Imprimir tabla de empleados en el perfil del jefe
@main.route('/tablas')
def tablas():
    return render_template('tables.html')

# Añadir vista en blanco    
@main.route("/vista")
def vista():
    return render_template('layout-sidenav-light.html')

# Añadir errores
@app.route("/error")
def error():
    return render_template('404.html')