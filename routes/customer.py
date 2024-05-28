from flask import Blueprint

customer_route = Blueprint('customer', __name__)

"""
Rota de customer

    - /customer/ (GET) - listar os clientes
    - /customer/ (POST) - inserir clientes no servidor 
    - /customer/new (GET) - renderizar o formulário para criar um cliente
    - /customer/<id> (GET) - obter dados de um cliente
    - /customer/<id>/edit (GET) - renderizar um formulário para editar um cliente
    - /customer/<id>/update (PUT) - atualizar os dados do cliente
    - /customer/<id>/delete (DELETE) - deleta o registro do usuário
"""

@customer_route.route('/', methods=['GET'])
def list_customer():
    """Listar os clientes"""
    return render_template('list_customer.html')

@customer_route.route('/', methods=['POST'])
def inserir_customer():
    """Inserir os dados do cliente"""
    pass

@customer_route.route('/new', methods=['GET'])
def form_customer():
    """Formulário para cadastrar um cliente"""
    return {'pagina': "form_customer"}

@customer_route.route('/<int:customer_id>', methods=['GET'])
def detalhe_customer(customer_id):
    """Exibir detalhes do cliente"""
    pass

@customer_route.route('/<int:customer_id>/edit', methods=['GET'])
def form_edit_customer(customer_id):
    """Formulário para editar um cliente"""
    pass

@customer_route.route('/<int:customer_id>/update', methods=['PUT'])
def update_customer(customer_id):
    """Atualizar informações de um cliente"""
    pass

@customer_route.route('/<int:customer_id>/delete', methods=['DELETE'])
def delete_customer(customer_id):
    """Deletar informações de um cliente"""
    pass

