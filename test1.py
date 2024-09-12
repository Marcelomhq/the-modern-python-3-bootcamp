class User:
    def __init__(self,first,last,age):
        self.first_name = first
        self.last_name = last
        self.age = age
    
user1 = User('Joe', 'Mama', 999999)
user2 = User('peter', 'Griffin', [1,2,3])
print(user1.first_name, user1.last_name, user1.age)
print(user2.last_name, user2.age[2])