# Visão Geral
Este projeto Backend, é uma aplicação web desenvolvida usando Flask, SQLAlchemy e PostgreSQL. 
O objetivo do projeto é gerenciar informações sobre vendedores, incluindo funcionalidades de CRUD 
(Create, Read, Update, Delete) e a capacidade de adicionar vendedores em lote a partir de uma planilha.

# Funcionalidades
  #Adicionar Vendedores: Cadastre novos vendedores com informações como nome, CPF, data de nascimento, email e estado (UF).<br>
  #Listar Vendedores: Veja a lista de todos os vendedores cadastrados no sistema.<br>
  #Atualizar Vendedores: Atualize as informações de vendedores existentes.<br>
  #Excluir Vendedores: Remova vendedores do sistema.<br>
  #Adicionar Vendedores em Lote: Carregue uma planilha com dados de vendedores para adicionar ou atualizar múltiplos registros de uma vez.<br>
  # Estrutura do Projeto<br>
  #O projeto está organizado da seguinte forma:

# app/: Contém a aplicação Flask.
  #models.py: Define a estrutura da tabela de vendedores e os métodos de serialização.<br>
  #routes.py: Define as rotas para interagir com a aplicação.<br>
  #init.py: Inicializa a aplicação e configura o banco de dados.<br>
  
 migrations/: Pasta gerada pelo Alembic para gerenciar as migrações do banco de dados.<br>
 uploads/: Pasta onde as planilhas de vendedores podem ser armazenadas para processamento.<br>
 venv/: Ambiente virtual para gerenciar as dependências do projeto.<br>
 alembic.ini: Configuração do Alembic para migrações do banco de dados.<br>
 requirements.txt: Lista de dependências do projeto.<br>

# Configuração e Execução
  Requisitos<br>
  Python 3.8+<br>
  PostgreSQL<br>
