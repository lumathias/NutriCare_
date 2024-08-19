#!/usr/bin/python3
from flask import Flask, request, jsonify
import mysql.connector
from os import environ
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# endpoints # CRUD - patient
# no read usar get 
# ao usar get não passar senha (dados sensiveis) - usar post
# pensar em ex de um nutricionista cadastrando paciente


# atividade 1 - criar instruções sql e popular as tabelas básicas 
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

# Configure your JWT secret key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key

# Initialize the JWT manager
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# python3 api-maria.py
# curl -X POST -H "Content-Type: application/json" -d @test-admin.json http://127.0.0.1:8080/login
# curl -H "Authorization: Bearer <meu_token>" http://127.0.0.1:8080/protected
# Your User model (adjust fields as needed)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) # Store hashed passwords
    
    with app.app_context():
        db.create_all() 

# Route to create a new token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    roles = ['nutri', 'paciente']
    if username == 'edu' and password=='123':
        access_token = create_access_token(identity=username, additional_claims={"roles": roles})
        return jsonify(access_token=access_token) 
    else:
        return jsonify({"msg": "Bad username or password"}), 401
    
# A protected route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    claims = get_jwt()
    roles = claims.get('roles', [])

    # Check if the user has the required role
    if 'prof' not in roles:
        return jsonify(msg="You do not have access to this resource"), 403

    #chamada ao BD

    return jsonify(logged_in_as=current_user, roles=roles), 200

if __name__ == '__main__':
    app.run(port=8080)

@app.route('/add_patient', methods=['POST'])
def add_patient_route():
    """Flask route to handle patient addition via POST requests."""
    try:
        data = request.get_json()
        # Extrai dados do pacient 
        cpf = data.get('cpf')
        nome = data.get('nome')
        genero = data.get('genero')
        email = data.get('email')
        senha = data.get('senha') 
        ficha = data.get('ficha')  # Optional, handle if not provided

        # Call your add_patient function
        add_patient(cpf, nome, genero, email, senha, ficha)

        return {'message': 'Patient added successfully'}, 201  # 201 Created status

    except ValueError as e:
        return {'error': str(e)}, 400  # 400 Bad Request for validation errors

    except mysql.connector.Error as e:
        return {'error': 'Database error'}, 500  # 500 Internal Server Error


##########################################################################################

@app.route('/add_patient', methods=['POST'])
def get_people_count():
    select_query = "SELECT * FROM PeopleCount"
    return run_select_query(select_query)

@app.route('/get_people_count_per_collector', methods=['GET'])
def get_people_count_per_collector():
    request_data = request.get_json()
    collectorId = request_data['collector_id']
    select_query = "SELECT * FROM PeopleCount WHERE collector_id = \'"+collectorId+"\'"
    return run_select_query(select_query)

@app.route('/get_people', methods=['GET'])
def get_ppl():
    select_query = "SELECT * FROM People"
    return run_select_query(select_query)

@app.route('/get_recognized', methods=['GET'])
def get_recog():
    select_query = "SELECT * FROM Recognized"
    return run_select_query(select_query)

@app.route('/get_people_recognized', methods=['GET'])
def get_people_recognized():
    select_query = "SELECT collector_id, timestamp, name FROM People INNER JOIN PeopleRecognized ON PeopleRecognized.id_people = People.id INNER JOIN Recognized ON PeopleRecognized.id_recognized = Recognized.id"
    return run_select_query(select_query)

@app.route('/add_people_count', methods=['POST'])
def add_people_count():
    print('Add people count called!')
    print('Request' + str(request.data))
    insert_query = """INSERT INTO PeopleCount (value, collector_id, timestamp) VALUES (%s, %s, %s)"""
    request_data = request.get_json()
    val = (request_data['value'],request_data['collector_id'],str(request_data['timestamp']))
    return run_insert_query(insert_query, val, 'PeopleCount')   

@app.route('/add_people_recognized', methods=['POST'])
def add_ppl_recognized():
    request_data = request.get_json()
    name_ids = []
    print('Request data (json): '+str(request_data['value']))
    for name in request_data['value']:
        print(name)          
        name_ids.append(add_people(name))

    recog_id = add_recognized(request_data)   
    res = []
    for name_id in name_ids:
        insert_query = """INSERT IGNORE INTO PeopleRecognized (id_recognized, id_people) VALUES (%s, %s)"""    
        val = (recog_id, name_id)        
        res.append(run_insert_query(insert_query, val, 'PeopleRecognized'))

    return json.dumps(res)

def add_people(name):
    insert_query = """INSERT IGNORE INTO People (name) VALUES (%s)"""    
    val = (name,)
    return run_insert_query(insert_query, val, 'People')[1]   #returns id

def add_recognized(request_data):
    insert_query = """INSERT INTO Recognized (collector_id, timestamp) VALUES (%s, %s)"""
    val = (request_data['collector_id'],str(request_data['timestamp']))
    return run_insert_query(insert_query, val, 'Recognized')[1]   #returns id
    
def get_database_connection():
    return mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

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
    return json.dumps(res)