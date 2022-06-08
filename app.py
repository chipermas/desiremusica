from flask import Flask
from flask import request
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from flask import session
from flask import flash

from config import DevelopmentConfig
from models import db
from models import User
from models import Cursos
from models import Clases


from flask import redirect
from flask import url_for

import form

app = Flask(__name__)   
app.config.from_object(DevelopmentConfig)
db.init_app(app)
with app.app_context():
    db.create_all()

csrf = CSRFProtect(app)

@app.errorhandler(404)
def page404(e):
    return render_template('404.html')
#Rutas
@app.route('/')
def index():
    cursos = Cursos.query.add_columns(Cursos.id, Cursos.curso, Cursos.descripcion, Cursos.imagen)    
    return render_template("index.html", cursos = cursos)
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = form.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():

        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username = username).first()
        
        if user is not None and user.verify__password(password):            
            
            session['username'] = login_form.username.data
            return redirect(url_for('cursos'))

        else:
            error_message = 'El usuario o el password son incorrectos'
            flash(error_message)

        
    return render_template("login.html", form = login_form)
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    registro_usuario_from = form.RegistroUsuarioForm(request.form)

    if request.method == 'POST' and registro_usuario_from.validate():
        
        user = User( 
        username = registro_usuario_from.username.data, 
        nombre = registro_usuario_from.nombre.data, 
        apellido = registro_usuario_from.apellido.data, 
        email = registro_usuario_from.email.data, 
        password = registro_usuario_from.password.data)

        db.session.add(user)
        db.session.commit()

        success_message = 'El usaurio fue registrado'
        flash(success_message)
        return redirect(url_for('login'))
        
    return render_template("registro.html", form = registro_usuario_from)

@app.route('/cursos')
def cursos():
    if 'username' in session: 
        cursos = Cursos.query.add_columns(Cursos.id, Cursos.curso, Cursos.descripcion, Cursos.imagen)

        return render_template('cursos.html', cursos = cursos)
        
    return redirect(url_for('login'))

@app.route('/cursos/<idcurso>')
def clases(idcurso):
    if 'username' in session:        
        clases = Clases.query.filter_by(curso_id = idcurso)
        
        return render_template('clases.html', clases = clases)
    return redirect(url_for('login'))

#Iniciador
if __name__ == '__main__':
    csrf.init_app(app)
    app.run()


# @app.route('/ajax-login', methods = ['POST'])
# def ajax_login():
#     print(request.form)
#     username = request.form['username']
#     response = {'status': 200, 'username': username, 'id': 1}
#     return json.dumps(response)