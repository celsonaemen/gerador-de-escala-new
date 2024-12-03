from main import db  # Importa o banco de dados diretamente de main.py

# Modelos de Banco de Dados
from models import (
    dupla_mot_tro_linh_fixa,
    horario_e_motorista_rio,
    horarios_manhuaçu,
    motorista_rodizio,
    trocadores_rodizio,
)

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    """Função para criar as tabelas no banco de dados"""
    db.create_all()  # Cria as tabelas definidas nos modelos

# Função para importar dados ou realizar qualquer ação necessária
def importar_dados():
    """Aqui você pode adicionar a lógica para importar dados das tabelas"""
    # Coloque seu código de importação aqui
    pass

# Chamando as funções
if __name__ == "__main__":
    criar_tabelas()  # Cria as tabelas no banco de dados
    importar_dados()  # Chama a função de importação dos dados
