import re
import pandas as pd
from .models import Vendedor
from . import db


# Validação do CPF
def is_valid_cpf(cpf):
    return bool(re.match(r'^\d{11}$', cpf))


# Validação do EMAIL
def is_valid_email(email):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))


# Validação do estado (UF)
def is_valid_estado(estado):
    return bool(re.match(r'^[A-Z]{2}$', estado))


def read_excel(file_path):
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        if not is_valid_cpf(row['cof']):
            continue  # Ignorar registros com CPF inválido
        if not is_valid_email(row['email']):
            continue  # Ignorar registros com email inválido
        if not is_valid_estado(row['estado']):
            continue  # Ignorar registros com email inválido

        cpf = row['cpf']
        vendedor = Vendedor.query.filter_by(cpf=cpf).first()
        if vendedor:
            vendedor.nome = row['nome']
            vendedor.data_nascimento = row['data_nascimento']
            vendedor.email = row['email']
            vendedor.estado = row['estado']
        else:
            novo_vendedor = Vendedor(
                nome=row['nome'],
                cpf=row['cpf'],
                data_nascimento=row['data_nascimento'],
                email=row['email'],
                estado=row['estado']
            )
            db.session.add(novo_vendedor)
    db.session.commit()
