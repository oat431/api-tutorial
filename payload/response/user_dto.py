from models.user import User

class UserDto :
    def __init__(self, user: User) :
        self.id = user.id
        self.name = user.firstname + ' ' + user.lastname
        self.email = user.email
        self.age = user.age
    
    @property
    def serialize(self) :
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }
