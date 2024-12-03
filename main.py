from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gerador_escalas.db'  # Usando SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Modelos de tabela
class MotoristaLinhaFixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    linha_fixa = db.Column(db.String(50), nullable=False)

class MotoristaRodizio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    rodizio = db.Column(db.String(50), nullable=False)

class TrocadorLinhaFixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    linha_fixa = db.Column(db.String(50), nullable=False)

class TrocadorRodizio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    rodizio = db.Column(db.String(50), nullable=False)

class HorarioFixo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(5), nullable=False)

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    with app.app_context():  # Contexto do Flask
        db.create_all()  # Cria as tabelas no banco de dados

# Função para importar dados ou realizar qualquer ação necessária
def importar_dados():
    """Aqui você pode adicionar a lógica para importar dados das tabelas"""
    # Exemplo de importação de dados: você pode fazer isso usando pandas ou outras bibliotecas
    pass  # Coloque seu código de importação aqui

# Chamando as funções
if __name__ == "__main__":
    criar_tabelas()  # Cria as tabelas no banco de dados
    importar_dados()  # Chama a função de importação dos dados
