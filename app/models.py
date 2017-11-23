user_database = {'karis.bm@gmail.com':'123456'}
events = []

from flask import Flask, session

class User(object):
    """all methods pertaining a user"""
    @staticmethod
    def register_user(email, password):
        """saving the user"""
        user_database[email] = password
        return "Registered"
       

    @staticmethod
    def user_exists(email):
        if user_database.get(email):
            return "Email already in use"

    @staticmethod
    def login(email, password):
        if user_database.get(email):
            if user_database[email] == password:
                return "User found"
            return "Wrong username or password"
        return "Username not found"
    
    @staticmethod
    def logout():
        session['logged_in'] = False


class UserEvent(object):
    """all methods for user events"""

    def __init__():
        # something here
        pass

