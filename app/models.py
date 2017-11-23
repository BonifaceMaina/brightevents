user_database = {'email':'password'}
user = []
events = {}



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
                if not user:
                    user.append(email)
                else:
                    user[0] = 'email'
                return "User found"
            else:
                return "Wrong password"
        else:
            return "Username not found"
    
    @staticmethod
    def logout():
        pass
class Events(object):
    """all operations associated with events"""

    @staticmethod
    def create_event(event):
        """check whether the user is in the events dictionary"""
        if user[0] not in events:
            """if user does not exist, initialize an empty list"""
            events[user[0]] = []
        if event in events.get((user[0])):
            return "That event already exists"
        events[user[0]].append(event)
        return "Event added"

    @staticmethod
    def get_events():
        if events:
            if events.get(user[0]):
                return events.get(user[0])
            else:
                return "You do not have events"
        else:
            return "There are no events"


