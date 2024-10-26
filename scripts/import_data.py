import csv
import os
import sys

# Adicione o caminho para o diretório raiz do projeto (onde estão app e scripts)
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from app import create_app
app = create_app()
from app import db
from scripts.create_tables import create_table
from app.models import UnidadeDeSaude

def import_csv(csv_file_path):
    import csv
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Crie seu objeto unidade aqui
            unidade = UnidadeDeSaude(
                capsi=row['capsi'],
                abrangencia=row['abrangencia'],
                endereco=row['endereco'],
                bairro=row['bairro'],
                cidade=row['cidade'],
                uf=row['uf'],
                contato=row['contato'],
                ramais=row['ramais'],
                contato2=row['contato2'],
                email=row['email'],
                isFullTime=row['isFulltime'] == 'TRUE',
                alcoolDrogas=row['alcoolDrogas'] == 'TRUE',
                transtornoGrave=row['transtornoGrave'] == 'TRUE',
                criancaAdolescente=row['criancaAdolescente'] == 'TRUE',
                observacao=row['observacao']
            )
            db.session.add(unidade)
        db.session.commit()

if __name__ == "__main__":
    csv_file_path = os.path.join(root_dir, 'data', 'UnidadesDeSaude.csv')
    with app.app_context():  # Create an application context
        create_table() 
        import_csv(csv_file_path)