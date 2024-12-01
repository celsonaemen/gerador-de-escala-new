from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'  # ou o URI do seu banco de dados
db = SQLAlchemy(app)

# Definição do modelo (se não estiver feito ainda)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))

# Agora, ao rodar o código abaixo, o db estará configurado
db.create_all()

 

class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(20), nullable=False, unique=True)
    horario_trabalho = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Motorista {self.nome}>'
