from app import create_app  # Importa a função create_app

app = create_app()  # Cria uma instância do app chamando create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Inicia o servidor