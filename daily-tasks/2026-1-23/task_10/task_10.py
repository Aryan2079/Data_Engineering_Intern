# task 10: Write a Python program to read a JSON file containing a list of users and print only their names.

import json

def read_json(filename):

    with open(filename,'r', encoding='utf-8') as f:
        users = json.load(f)
        for user in users:
            print(f"name: {user['name']}")

read_json('test.json')