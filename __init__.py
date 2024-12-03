from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gerador_escalas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com o aplicativo
    db.init_app(app)

    # Importa os modelos para registrar no SQLAlchemy
    with app.app_context():
        from app import models  # Importa os modelos
        db.create_all()  # Cria as tabelas

    return app
