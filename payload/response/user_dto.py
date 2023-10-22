from models.user import User
import datetime

class UserDto :
    def __init__(self, user: User) :
        self.id = user.id
        self.name = user.firstname + ' ' + user.lastname
        self.email = user.email
        self.age = self.__get_age(user.birth_date)
    
    @property
    def serialize(self) :
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }
    
    def __get_age(self, birth_date:str) -> int:
        current_year = datetime.datetime.now().year
        user_birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        age = current_year - user_birth_date.year
        return age
    
