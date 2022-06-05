from django.contrib.auth.models import User

def authenticate(data):
    # TODO: add login urls here
    return User(username="user", password="somepasswordhash", is_active=True)
