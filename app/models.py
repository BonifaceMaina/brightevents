user_database = {}
myevents = {}
otherevents = {}



class User(object):
    """all methods pertaining a user"""

    
    def __init__(self):
        # something goes here

    def register_user(self, name, email, password):
        if user_database.get(email):
            return "Email exists. Use another"
        else:
            user_database[user] = password
        return "Registration successful"

        #add user

class UserEvent(object):
    """all methods for user events"""

    def __init__(self, name, caategory, location, date, description):
        # something here

    def create_event(self):
        # something here

    def edit_event(self):
        # something else

    def delete_event(self):
        # something here

    def show_personal_events(self):
        # something here

    def rsvp():

    def show_rsvpd(self):
        # something here


class OtherEvents(object):
    """methods for all other events"""

    def show_event(self):
        # something here

    def show_all(self):
        # something else