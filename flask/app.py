from flask import Flask, request, render_template, session, url_for, jsonify
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key ='Mi_llave_secreta'

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login: {session["username"]} '
    return 'No ha hecho login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<name>')
def saludar(name):
    return f'Saludos {name.title()}'

@app.route('/edad/<int:age>')
def showEdad(age):
    return f'Tu edad es: {age}'

@app.route('/mostrar/<name>', methods=['GET', 'POST'])
def showName(name):
    return render_template('show.html', name=name)

# redireccionar
@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('showName', name='Andres'))

# manejo de errores
@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def error404(error):
    return (render_template('error404.html', error=error), 404)

# uso de REST
@app.route('/api/mostrar/<name>', methods=['GET', 'POST'])
def mostrarJson(name):
    values = {'name':name,
              'metodo_http': request.method}
    return jsonify(values)