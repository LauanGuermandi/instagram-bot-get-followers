import json
import os


class Config:
    username = ''
    password = ''

    def __init__(self):
        path = os.path.abspath('config.json')
        if not os.path.isfile(path):
            print('Config file doesn\'t exists!')
            return
        with open(path) as json_file:
            config = json.load(json_file)
            self.username = config['username']
            self.password = config['password']

