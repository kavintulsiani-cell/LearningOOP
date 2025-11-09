class User :
    def __init__(self, name, birthyear):
        self.birthyear = birthyear
        self.name = name



    def get_name ( self ):
        pass

    def age ( self, current_year ):

        user_age = current_year - self.birthyear
        return user_age

    def get_age ( self, current_year ):
        self.current_year = 2025

user_ages = User ("John", 1972)
final_age = user_ages.age (2025)
print (f" {user_ages.name} is  {final_age} years old.")




