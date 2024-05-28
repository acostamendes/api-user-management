from flask import Blueprint, render_template, request, jsonify
from database.customer import CUSTOMER

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
    return render_template('list_customer.html', customer=CUSTOMER)

@customer_route.route('/', methods=['POST'])
def inserir_customer():
    """Inserir os dados do cliente"""
    data = request.json

    new_usuario = {
        "id": len(CUSTOMER) + 1,
        "nome": data['name'] ,
        "name": data['email'] ,
    }

    CUSTOMER.append(new_usuario)

    # Você pode adicionar a lógica para inserir o cliente aqui
    return render_template('item_customer.html', customer=new_usuario)
#jsonify({'C': "Cliente inserido com sucesso"}), 200

@customer_route.route('/new', methods=['GET'])
def form_customer():
    """Formulário para cadastrar um cliente"""
    return render_template('form_customer.html')

@customer_route.route('/<int:customer_id>', methods=['GET'])
def detalhe_customer(customer_id):
    """Exibir detalhes do cliente"""
    return render_template('detalhe_customer.html')

@customer_route.route('/<int:customer_id>/edit', methods=['GET'])
def form_edit_customer(customer_id):
    """Formulário para editar um cliente"""
    return render_template('form_edit_customer.html')

@customer_route.route('/<int:customer_id>/update', methods=['PUT'])
def update_customer(customer_id):
    """Atualizar informações de um cliente"""
    pass

@customer_route.route('/<int:customer_id>/delete', methods=['DELETE'])
def delete_customer(customer_id):
    """Deletar informações de um cliente"""
    pass


