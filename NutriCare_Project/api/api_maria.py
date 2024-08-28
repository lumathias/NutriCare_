#!/usr/bin/python3
from flask import Flask, request, jsonify
import mysql.connector, secrets, json
from os import environ
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL

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
DB_PASSWORD = environ.get('DB_PASSWORD') # root

if DB_PASSWORD is not None:
    print('###################################')
    print('These are the environment variables: DB_HOST='+DB_HOST+', DB_NAME='+DB_NAME+', DB_USER='+DB_USER+', DB_PASSWORD='+DB_PASSWORD)
    print('###################################')
else:
    print('###################################')
    print('No environment variable appeared!')
    print('###################################')

db = DB_NAME #Não sei se isso aqui faz sentido#
app = Flask(__name__)
app.config['MYSQL_DB'] = 'flask'

# Configuração da chave JWT secreta 
jwt_secret_key = secrets.token_hex(32)  # 32 bytes = 256 bits
app.config['JWT_SECRET_KEY'] = jwt_secret_key # Gera uma chave criptograficamente segura

# Inicialização do JWT manager e outros
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
mysql = MySQL(app)

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
    cursor.execute("SELECT senha FROM paciente WHERE nome = %s", (email))
    paciente = cursor.fetchone()
    if paciente and paciente['senha'] == password:
        return "paciente"
    
    # Verifica na tabela de nutricionistas
    cursor.execute("SELECT senha FROM nutricionista WHERE username = %s", (email))
    nutricionista = cursor.fetchone() 
    if nutricionista and nutricionista['senha'] == password:
        return "nutricionista"
    return None

# cria um novo token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    role = check_user_credentials(username, password)
    if role:
        roles = [role]
        access_token = create_access_token(identity=username, additional_claims={"roles": roles})
        return jsonify(access_token=access_token) 
    else:
        return jsonify({"msg": "Usuário ou senha incorreta."}), 401

'''# rota protegida
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Acessa a identidade do usuario atual com get_jwt_identity
    current_user = get_jwt_identity()
    claims = get_jwt()
    roles = claims.get('roles', [])

    # Checa se user tem o role necessário
    if 'claims' not in roles:
        return jsonify(msg="Access denied"), 403

    #chamada ao BD
    return jsonify(logged_in_as=current_user, roles=roles), 200'''

# Registra novo paciente
@app.route('/register_patient', methods=['POST'])
@jwt_required()
def register_patient():
    data = request.get_json()
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    query = """
    INSERT INTO paciente (username, email, senha, cpf, genero, ficha)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (data['username'], data['email'], hashed_password, data['CPF'], data['genero'], data.get('ficha'))
    
    _, id = run_insert_query(query, values, 'paciente')
    
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
    
    # Obter o id do nutricionista a partir do usuário
    cursor.execute("SELECT id FROM nutricionista WHERE username = %s", (current_user))
    nutricionista = cursor.fetchone()
    
    if not nutricionista:
        return jsonify({"msg": "Nutricionista não encontrado."}), 404
    
    nutricionista_id = nutricionista['id']
    
    # Listar os pacientes associados a esse nutricionista
    cursor.execute("SELECT id, nome FROM paciente WHERE nutricionista_id = %s", (nutricionista_id))
    pacientes = cursor.fetchall()
    
    return jsonify(pacientes=pacientes)

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