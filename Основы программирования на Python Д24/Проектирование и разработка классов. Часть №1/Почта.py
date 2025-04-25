from collections import defaultdict
from datetime import datetime


def check_password_strength(password):
    if len(password) < 8:
        raise ValueError('A password must be at least 8 characters long')
    if not any(el.isdigit() for el in password):
        raise ValueError('A password must contain a digit')


class User:
    def __init__(self, name, email, password):
        self.username, self.email, self.password = name, email, password
        self.connected_to = None

    def change_username(self, new_username):
        self.username = new_username

    def change_password(self, old_password, new_password):
        if old_password != self.password:
            raise ValueError('Incorrect password. Please provide the correct current password to verify your identity.')
        check_password_strength(new_password)
        self.password = new_password

    def send_message(self, server, user, message):
        if not self.connected_to:
            raise ValueError('You are not connected to any server')
        if user not in server.users:
            raise ValueError('User not found in the selected server')
        server.mail_pending[user].add(message)

    def connect_to(self, server):
        self.connected_to = server
        server.users.add(self)

    def receive_mail(self):
        if not self.connected_to:
            raise ValueError('You are not connected to any server')
        if not self.connected_to.is_under_maintenance:
            return self.connected_to.mail_pending[self]
        return ValueError('Server is currently under maintenance')


class Message:
    def __init__(self, sender, contents):
        self.sender = sender
        self.contents = contents
        self.timestamp = datetime.now()

    def __hash__(self):
        return hash(self.contents + str(datetime.now()))


class Server:
    def __init__(self, name, users=None):
        self.name = name
        self.users = set(users) if users else set()
        self.is_under_maintenance = False
        self.mail_pending = defaultdict(set)

    def close_for_maintenance(self):
        self.is_under_maintenance = True

    def end_maintenance(self):
        self.is_under_maintenance = False


servers = defaultdict(Server)