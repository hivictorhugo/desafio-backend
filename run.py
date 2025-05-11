from app import create_app

# Criar a app usando a função create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
