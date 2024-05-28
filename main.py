from flask import Flask
from routes.home import home_route
from routes.customer import customer_route

# Inicialização
app = Flask(__name__)

# Rotas
app.register_blueprint(home_route)
app.register_blueprint(customer_route, url_prefix='/customer')

# Execução
if __name__ == '__main__':
    app.run(debug=True)


