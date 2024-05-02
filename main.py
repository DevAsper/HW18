class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'User ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}'


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._user_list.append(user)
            print(f'User {user.get_name()} added successfully.')
        else:
            print("Failed to add user. Invalid user type.")

    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f'User {user.get_name()} removed successfully.')
                return
        print("User not found.")

    def list_users(self):
        for user in self._user_list:
            print(user)

admin = Admin(1, 'Alice')
user1 = User(2, 'Bob')
user2 = User(3, 'Charlie')

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(2)
admin.list_users()
