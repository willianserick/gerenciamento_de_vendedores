from flask import request, jsonify, current_app
from . import db
from .models import Vendedor
from .utils import is_valid_cpf, is_valid_email, is_valid_estado, read_excel
from sqlalchemy.exc import IntegrityError
import os


@current_app.route('/vendedores/cadastrar', methods=['POST'])
def cadastrar_vendedores():
    data = request.json
    if not is_valid_cpf(data['cpf']):
        return jsonify({"error": "CPF inválido"}), 400
    if not is_valid_email(data['email']):
        return jsonify({"error": "Email inválido"}), 400
    if not is_valid_estado(data['estado']):
        return jsonify({"error": "Estado (UF) inválido"}), 400

    try:
        novo_vendedor = Vendedor(
            nome=data['nome'],
            cpf=data['cpf'],
            data_nascimento=data['data_nascimento'],
            email=data['email'],
            estado=data['estado'],
        )
        db.session.add(novo_vendedor)
        db.session.commit()
        return jsonify({'message': 'Vendedor cadastrado com sucesso'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'CPF já existe'}), 409


@current_app.route('/vendedores', methods=['GET'])
def get_vendedores():
    vendedores = Vendedor.query.all()
    return jsonify([vendedor.serialize() for vendedor in vendedores])


@current_app.route('/vendedores/<int:id>', methods=['GET'])
def get_vendedor(id):
    vendedor = Vendedor.query.get_or_404(id)
    return jsonify(vendedor.serialize())


@current_app.route('/vendedores/alter/<int:id>', methods=['PUT'])
def update_vendedor(id):
    data = request.json
    if not is_valid_cpf(data['cpf']):
        return jsonify({"error": "CPF inválido"}), 400
    if not is_valid_email(data['email']):
        return jsonify({"error": "Email inválido"}), 400
    if not is_valid_estado(data['estado']):
        return jsonify({"error": "Estado (UF) inválido"}), 400

    vendedor = Vendedor.query.get_or_404(id)
    vendedor.nome = data['nome']
    vendedor.cpf = data['cpf']
    vendedor.data_nascimento = data['data_nascimento']
    vendedor.email = data['email']
    vendedor.estado = data['estado']
    db.session.commit()
    return jsonify({'message': 'Vendedor atualizado com sucesso'}), 200


@current_app.route('/vendedores/delete/<int:id>', methods=['DELETE'])
def delete_vendedor(id):
    vendedor = Vendedor.query.get_or_404(id)
    db.session.delete(vendedor)
    db.session.commit()
    return jsonify({'message': 'Vendedor deletado com sucesso'}), 200


@current_app.route('/vendedores/cadastrar-lote', methods=['POST'])
def upload_vendedores():
    file = request.files['file']
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    read_excel(file_path)
    return jsonify({"message": "Vendedores adicionados com sucesso"}), 200
