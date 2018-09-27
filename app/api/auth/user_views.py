import psycopg2
import jwt
from functools import wraps
import datetime
from . import AUTH
from instance.config import Config
from .user_models import Users
from ...db.db import connect
from flask import request, jsonify, make_response

secret = Config().SECRET_KEY

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return {'message':'Token is missing'}, 403
        try:
            data = jwt.decode(token, secret)
            current_user = data
        except:
            return {"message":"Token is invalid"}, 403
        return f(args, **kwargs)
    return decorated

def token_required_jsonify(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message':'Token is missing'}), 403
        try:
            data = jwt.decode(token, secret)
            current_user = data
        except:
            return jsonify({"message":"Token is invalid"}), 403
        return f(current_user, *args, **kwargs)
    return decorated


@AUTH.route('/users', methods=['GET'])
@token_required_jsonify
def get_all_users(current_user):

    role = current_user['role']
    if role != 'admin':
        return jsonify({"Sorry": "Route restricted to admin only"})

    query = Users.get_all_users_query()
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    
    return jsonify({"Users" : rows})

@AUTH.route('/users/<user_id>', methods=['GET'])
@token_required_jsonify
def get_one_user_id(current_user, user_id):

    query = Users.get_user_query_id(user_id)
    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()

    user = row
    return jsonify({"User": row})


@AUTH.route('/users', methods=['POST'])
def create_user():    
    try:
        data = request.get_json()
        query = Users.insert_user_query(data)
        user = data['username']
        conn = connect()
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.commit()
        success_message = """ User {} Created""".format(user)        
        return  jsonify({"Success": success_message})
    except KeyError:
        return jsonify({"Error":"you did not enter data correctly"})  
        
    

@AUTH.route('/login', methods=['POST'])
def login_user():

    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    query = Users.get_user_query(auth.username)

    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    row = cur.fetchone()

    if not row:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    dbusername = row[0]
    dbpassword = row[1]
    dbrole = row[2]
    
    if auth.password != dbpassword:
        return jsonify({"Error":"Invalid Password"})
    token = jwt.encode({'user': dbusername, 'role': dbrole, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, secret)

    return jsonify({"token": token.decode('UTF-8')})

