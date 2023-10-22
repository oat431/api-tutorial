from models.user import User

class UserDto :
    def __init__(self, user: User) :
        self.name = user.firstname + ' ' + user.lastname
        self.email = user.email
        self.age = user.age
    
    @property
    def serialize(self) :
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age
        }