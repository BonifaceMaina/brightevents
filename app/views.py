from flask import request, jsonify, session, json
from app import app
from app.models import User, UserEvent


@app.route('/api/auth/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = str(request.json.get('email'))
        password = request.data.get('password')
        if User.user_exists(email) == "Email already in use":
            return jsonify({'message': 'Email already taken'})
        if User.register_user(email, password) == "Registered":
            return jsonify({'message': 'Registration successful'})
    return jsonify({'message': 'Registration successful'})



@app.route('/api/auth/login', methods=['POST'])
def login():
    email = str(request.data.get('email', ''))
    password = '123456'
    if User.login(email, password) == "User found":
        session['logged in'] = True
        return jsonify({'message':'Login successful'})
    elif User.login(email, password) == "Wrong username or password":
        return jsonify({'message':'Wrong username or password'})     
    else:
        return jsonify({'message':"You are not registered"})   


@app.route('/api/auth/reset-password', methods=['POST'])
def resetpassword():
    pass

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    if User.logout():
        return jsonify({'message': 'You are logged out'})
    
    return jsonify({'message':'You are not logged in '})


@app.route('/api/events', methods=['POST', 'GET'])
def events():
    if request.method == 'POST':
        if session['logged_in']:
            if User.getEvents():
                pass
            pass
        pass
    pass


@app.route('/api/events/<eventId>', methods=['PUT'])
def event():
    pass

@app.route('/api/events/<eventId>', methods=['DELETE'])
def editevent():
    pass

@app.route('/api/event/<eventId>/rsvp')
def rsvp():
    pass
