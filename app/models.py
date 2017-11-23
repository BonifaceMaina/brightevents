user_database = {'email':'password'}
events = []


from flask import Flask, session

class User(object):
    """all operations pertaining a user"""
    @staticmethod
    def register_user(email, password):
        """saving the user"""
        if user_database.get(email):
            return "Email already in use"
        else:
            user_database[email] = password
            return "Registered"

    @staticmethod
    def login(email, password):
        if user_database.get(email):
            if user_database[email] == password:
                return "User found"
            else:
                return "Wrong username or password"
        else:
            return "Username not found"
    
    @staticmethod
    def logout():
        session['logged_in'] = False

class Events(object):
    """all operations associated with events"""

