import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db, create_app
from app.models import UnidadeDeSaude

app = create_app()

def create_table():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_table()
    print("Tabelas criadas com sucesso!")
