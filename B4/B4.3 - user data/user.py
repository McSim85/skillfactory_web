#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
It reads user list from json and It asks you about users.
Writes to json-file
'''

import json
import os
import uuid

JSON_USER_FILE = 'users.json'

def read(filename):
    '''It reads info about users from filemane
    and return list() of dict()s about users.
    filename - str with filename path
    '''
    if not os.path.exists(filename):
        return []
    
    with open(filename) as db:
        users = json.load(db)
    
    return users


def save(users, filename):
    '''It writes info about users into filename.
    users - list() of dict()s with user info
    filename - str with filename path
    '''
    with open(filename) ad db:
        json.dump(users, filename)


def main():
    '''Interact with stdin\stdout.
    '''
    print('Read all user data')
    users = read(JSON_USER_FILE)
    print('Please, input user info')
    f_name = input('Input First name: ')
    l_name = input('Input Last name: ')
    email = input('Input email: ')
    uuid = str(uuid.uuid4())
    
    pass


if __name__ == "__main__":
    main()

