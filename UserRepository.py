import os
import json
import shutil
import subprocess
from exceptions import UserAlreadyExistError

class UserRepository:

    def saveUser(username, email, password, state):
        with open(state.users_json_path, 'r') as file:
            users_data = json.load(file)

        if not username in users_data['users']:

            users_data['users'].append(username)

            with open(state.users_json_path, 'w') as file:
                json.dump(users_data, file)

            user_path = os.path.join(state.users_data_path, username)

            if os.path.isdir(user_path):
                shutil.rmtree(user_path)

            os.mkdir(user_path)

            user_index = len(users_data['users']) - 1
            user_data = {'index': user_index, 'email': email, 'pass': password, 'stories': [], 'fav_authors': [],
                         'fav_stories': []}

            user_json_path = os.path.join(user_path, 'user_data.json')

            with open(user_json_path, 'w') as file:
                json.dump(user_data, file)
        else:
            raise UserAlreadyExistError(username, email)