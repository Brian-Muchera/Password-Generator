class User:
    user_list = []

    def __init__(self,first_name,last_name,phone_number,email,username,password):


        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

        user_list = []
    def save_user(self):
        User.user_list.append(self)
        
    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
    
     for user in cls.user_list:
        if user.phone_number == number:
            return user

    @classmethod
    def user_exist(cls,number):
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False

    @classmethod
    def display_users(cls):
        return cls.user_list