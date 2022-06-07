from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime

db = SQLAlchemy()

progreso = db.table('progreso')

class User(db.Model):

    __tablename__ ='users'
     
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), unique=True, nullable=False)
    nombre = db.Column(db.String(66), nullable=False)
    apellido = db.Column(db.String(66), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default = datetime.datetime.now, nullable=False)

    def __init__(self, username, nombre, apellido, email, password):
        self.username =username
        self.nombre =nombre
        self.apellido =apellido
        self.email =email
        self.password = self.__create_password(password)
    
    def __create_password(self, password):
        return generate_password_hash(password)

    def verify__password(self, password):
        return  check_password_hash(self.password, password)

class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String(66), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    imagen = db.Column(db.String(80), nullable=False)
    #forein key
    clases = db.relationship('Clases', backref='curse')

    def __init__(self, curso, descripcion, imagen):
        self.curso = curso
        self.descripcion = descripcion
        self.imagen = imagen

class Clases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clase = db.Column(db.String(66), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    video = db.Column(db.String(80),nullable=False)
    #foreing key
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    
    archivos = db.relationship('Archivos', backref = 'class')

    def __init__(self, clase, descripcion, video):
        self.curso = clase
        self.descripcion = descripcion
        self.video = video

class Archivos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), nullable=False)
    #foreing key
    clase_id = db.Column(db.Integer, db.ForeignKey('clases.id'), nullable=False)
    def __init__(self, url):
        self.url = url



       