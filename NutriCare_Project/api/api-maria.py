#!/usr/bin/python3
from flask import Flask, request, jsonify
import mysql.connector, secrets, json
from os import environ
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import datetime 

# ativ. 1 - criar instruções sql e popular as tabelas básicas 
# 1.1 - nutricionista, paciente, alimento
# ativ. 2 - criar endpoint de autenticação
# 2.1 - rota tipo post, para que a senha não apareça na url
# 2.2 - criar token de especificaação de role (nutri ou paciente)
# ativ. 3 - criar endpoint para listar pacientes associados a um nutri
# 3.1 - acessar os ids dos pacientes 
# ativ. 4 - criar endpoint pra cadastro de plano alimentar de paciente
# 4.1 - o json do endpoint plano alimentar recebe (idNutri, idPaciente, listaRefeiçoes) 
# ativ. 5 - criar endpoint para listar plano alimentar 
# passar o idPaciente para esse endpoint

DB_HOST = environ.get('DB_HOST') # db 
DB_NAME = environ.get('DB_NAME') # nutricare
DB_USER = environ.get('DB_USER') # root
DB_PASSWORD = environ.get('DB_PASSWORD') # senha123

if DB_PASSWORD is not None:
    print('###################################')
    print('These are the environment variables: DB_HOST='+DB_HOST+', DB_NAME='+DB_NAME+', DB_USER='+DB_USER+', DB_PASSWORD='+DB_PASSWORD)
    print('###################################')
else:
    print('###################################')
    print('No environment variable appeared!')
    print('###################################')

app = Flask(__name__)

# Configuração da chave JWT secreta 
jwt_secret_key = secrets.token_hex(32)  # 32 bytes = 256 bits
app.config['JWT_SECRET_KEY'] = jwt_secret_key # Gera uma chave criptograficamente segura

# Inicialização do JWT manager e outros
jwt = JWTManager(app)

# python3 api-maria.py
# curl -X POST -H "Content-Type: application/json" -d @test-admin.json http://127.0.0.1:8080/login
# curl -H "Authorization: Bearer <meu_token>" http://127.0.0.1:8080/protected
# Your User model (adjust fields as needed)

def get_database_connection():
    return mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

def check_user_credentials(email, password):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Verifica na tabela de pacientes
    emails = [email]
    cursor.execute("SELECT senha FROM Paciente WHERE email = %s", (emails))
    pacient = cursor.fetchone()
    if pacient and pacient['senha'] == password:
        return "paciente"

    # Verifica na tabela de nutricionistas
    cursor.execute("SELECT senha FROM Nutricionista WHERE email = %s", (emails))
    nutri = cursor.fetchone() 
    if nutri and nutri['senha'] == password:
        return "nutricionista"
    return None

# cria um novo token = login
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('senha', None)

    role = check_user_credentials(email, password)
    if role:        
        roles = [role]
        access_token = create_access_token(identity=email, additional_claims={"roles": roles})
        return jsonify(access_token=access_token) 
    else:
        return jsonify({"msg": "Usuário ou senha incorreta."}), 401

# Registra novo paciente
@app.route('/register_patiente', methods=['POST'])
@jwt_required()
def register_patiente():
    current_user = get_jwt_identity()
    
    # Conectar ao banco de dados
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    
    data = request.get_json()
    
    query = """
    INSERT INTO Paciente (nome, email, senha, cpf, genero)
    VALUES (%s, %s, %s, %s, %s)
    """
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    values = (data['nome'], data['email'], hashed_password, data['CPF'], data['genero'])
    id = run_insert_query(query, values, 'Paciente')
    
    if id:
        return jsonify({'message': 'Usuário registrado com sucesso!'}), 201
    else:
        return jsonify({'error': 'Falha ao registrar usuário'}), 500
        
# Listar os pacientes associados a um nutricionista
@app.route('/pacientes', methods=['GET'])
@jwt_required()
def listar_pacientes():
    current_user = get_jwt_identity()
    
    # Conectar ao banco de dados
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Obtem id do nutri a partir do usuário
    cursor.execute("SELECT id FROM Nutricionista WHERE email = %s", (current_user))
    nutri = cursor.fetchone()
    
    if not nutri: # Caso n seja nutri
        return jsonify({"msg": "Nutricionista não encontrado."}), 404
    
    # Lista os pacientes associados ao nutri
    nutri_id = nutri['id']
    cursor.execute("SELECT id, nome FROM Paciente WHERE nutri.id = %s", (nutri_id))
    pacientes = cursor.fetchall()
    
    return jsonify(pacientes=pacientes)

# Registra nova avaliação
@app.route('/measurements', methods=['POST'])
@jwt_required()
def measurements():
    current_user = get_jwt_identity()
    
    # Conectar ao banco de dados
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    
    data = request.get_json()
    
    imc = data['peso'] / (data['altura'] * data['altura']) # Calcula o IMC  
    dataAtual = datetime.now().strftime('%Y-%m-%d') # data atual
    
    query = """
    INSERT INTO Avaliacao (peso, altura, imc, gordura, dataConsulta)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (data['peso'], data['altura'], imc, data['gordura'], dataAtual)  # Prepara valores para inserir
    
    _, id = run_insert_query(query, values, 'Avaliacao') # Executa a query e obtém o ID do registro inserido
    
    if id: # Retorna a resposta com base no resultado da inserção
        return jsonify({'message': 'Avaliação registrada!'}), 201
    else:
        return jsonify({'error': 'Falha ao registrar avaliação'}), 500

# Cadastra plano alimentar
@app.route('/plano-alimentar', methods=['POST'])
@jwt_required()
def cadastrar_plano_alimentar():
    data = request.get_json()
    id_nutri = data.get('idNutri')
    id_paciente = data.get('idPaciente')
    lista_refeicoes = data.get('listaRefeiçoes')

    current_user = get_jwt_identity()  # Verifica se o nutri autenticado é o do plano 
    
    # Conecta ao banco de dados
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT id FROM Nutricionista WHERE email = %s", (current_user))
    nutri = cursor.fetchone()
    
    if not nutri or nutri['id'] != id_nutri:
        return jsonify({"msg": "Ação não autorizada"}), 403
    
    # Adiciona o plano alimentar ao banco de dados
    plano_id = add_plano_alimentar( id_paciente, id_nutri, lista_refeicoes)
    
    return jsonify({"msg": "Plano alimentar cadastrado com sucesso ", "plano_id": plano_id}), 201

# Adicionar plano alimentar ao banco de dados
def add_plano_alimentar(id_paciente, id_nutri, lista_refeicoes):
    # Conectar ao banco de dados
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    # Inserir o plano alimentar na tabela
    cursor.execute("""
        INSERT INTO PlanoAlimentar (idNutri, idPaciente, refeicoes)
        VALUES (%s, %s, %s)
    """, (id_nutri, id_paciente, json.dumps(lista_refeicoes)))

    connection.commit()
    cursor.close()
    connection.close()

    return cursor.lastrowid

def run_insert_query(query, values, table_name):
    connection = get_database_connection()
    res = ''
    id = None
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        id = cursor.lastrowid
        if id is not None:
            res += 'Record with id('+str(id)+') inserted successfully into '+table_name+' table'
        else: 
            res += str(cursor.rowcount) + ' Record inserted successfully into '+table_name+' table'
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res += "Failed to insert record into table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return (res,id)

def run_select_query(query):
    connection = get_database_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        for x in res:
            print(x)
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res = "Failed to select from table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return jsonify.dumps(res)

########################################################################################

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=8080)