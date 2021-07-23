from werkzeug.utils import redirect
from forms import PersonaForm
from flask import Flask, request, render_template, url_for
from database import db
from flask_migrate import Migrate
from models import Persona

app = Flask(__name__)
# configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializacion del objeto db de sqlalchemy
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

# configuracion del flask-wtf
app.config['SECRET_KEY']='secret_key'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    app.logger.debug(f'Listado personas: {personas}')
    app.logger.debug(f'Total personas: {total_personas}')

    return render_template('index.html', personas=personas, total_personas=total_personas)

@app.route('/view/<int:id>')
def view(id):
    #Recuperamos la persona segun id
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('view.html', persona=persona)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar: {persona}')
            # insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('add.html', form = personaForm)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # recuperamos el objeto de la persona a editar
    persona = Persona.query.get_or_404(id)
    FormularioPersona = PersonaForm(obj=persona)
    if request.method == 'POST':
        if FormularioPersona.validate_on_submit():
            FormularioPersona.populate_obj(persona)
            app.logger.debug(f'Persona a actualizar: {persona}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('edit.html', form = FormularioPersona)

@app.route('/delete/<int:id>')
def delete(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
