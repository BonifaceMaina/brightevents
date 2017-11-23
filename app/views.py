from flask import request, jsonify, session, json
from app import app
from app.models import User, Events


@app.route('/api/auth/register', methods=['POST'])
def register():
    """route to register the user based on input sent"""
    email = request.args.get('email')
    password = request.args.get('password')
    """check whether email and password were inputted"""
    if email and password:
        """check whether email added already exists in dictionary, add them if not"""
        if User.register_user(email, password) == "Email already in use":
            return jsonify({'message': 'Email already taken'})
        elif User.register_user(email, password) == "Registered":
            return jsonify({'message': 'Registration successful'})
    return jsonify({'status_code':400})


@app.route('/api/auth/login', methods=['POST'])
def login():
    """login the user"""
    email = request.args.get('email')
    password = request.args.get('password')
    """check that email and password were added"""
    if email and password:
        """check if email provided exists"""
        if User.login(email, password) == "User found":
            session['logged in'] = True
            return jsonify({'message':'Login successful'})
            """compare passwords for the email provided"""
        elif User.login(email, password) == "Wrong username or password":
            return jsonify({'message':'Wrong username or password'})     
        else:
            return jsonify({'message':"You are not registered"})  
    else:
        return jsonify({'status_code':400})


@app.route('/api/auth/reset-password', methods=['POST'])
def resetpassword():
    """resetting the password for the user"""
    pass

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """logging out the user"""
    if User.logout():
        return jsonify({'message': 'You are logged out'})
    
    return jsonify({'message':'You are not logged in '})


@app.route('/api/events', methods=['POST', 'GET'])
def events():
    """getting all events pertaining a user"""
    if request.method == 'POST':
        event = request.args.get('event')
        if Events.create_event(event) == "That event already exists":
                return jsonify({'message': 'That event already exists'})
        else:
            if Events.create_event(event) == "Event added":
                return jsonify("Event Added")
    else:
        if Events.get_events() == "You do not have events":
            return jsonify({'message':'You do not have events'})
        else:
            if Events.get_events() == "There are no events":
                return jsonify({'message':'There are no events to show'})



@app.route('/api/events/<eventId>', methods=['PUT'])
def event():
    """get each individual event"""
    pass

@app.route('/api/events/<eventId>', methods=['DELETE'])
def deleteevent():
    """deleting individual events"""
    pass

@app.route('/api/events/<eventId>', methods=['DELETE'])
def editevent():
    """editing individual events"""
    pass

@app.route('/api/event/<eventId>/rsvp')
def rsvp():
    pass
