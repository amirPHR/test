class Informations:

    def __init__(self, username, password):
        self.username = username
        self.password = password 

    def check_password(self):
        if len(self.password) < 5:
            return f"your password is short" 
        return f""