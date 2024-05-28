from flask import Flask # metódo flask, importando a Class Flask, importando a função url_for, render_template - ler o arquivo .html
from routes.home import home_route
from routes.customer import customer_route


#incialização
app = Flask(__name__) # incializar o servidor

#rotas
app.register_blueprint(home_route)
app.register_blueprint(customer_route, url_prefix="/customer")
#rotas

#@app.route('/', methods=['GET', 'POST', 'PUT'])
#rota principal


# execucao  
app.run(debug=True) # modo desenvolvedor (Relatório Detalhado de Erros; Auto recarregamento, Console interativo, facilita a localização de bugs e melhora a eficiencia no desenvolvimento)
# localhost = 127.0.0.1 -> ip local; :5000 -> porta


#app.run(debug=True, port=80) definido a porta como 80

