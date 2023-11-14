import uuid


class UserEntity:
    def __init__(self, id:uuid, firstName:str, lastName:str, email:str):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        
    def __repr__(self):
        return f"User(user_id={self.id}, firstName='{self.firstName}', lastName='{self.lastName}', email='{self.email}')"
