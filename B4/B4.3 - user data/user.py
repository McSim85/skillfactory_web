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
    # print(os.path.exists(filename) and os.path.getsize(filename))
    if not os.path.exists(filename) or os.path.getsize(filename) == 0 :
        return []
    
    with open(filename) as db:
        users = json.load(db)
    
    return users


def save(users, filename):
    '''It writes info about users into filename.
    users - list() of dict()s with user info
    filename - str with filename path
    '''
    with open(filename, 'w') as db:
        json.dump(users, db)

def find(user, users):
    '''It find user in DB by name '''
    for a_user in users:
        if a_user['first_name'] == user: return a_user
        
def valid_email(email):
    '''Проверяет наличие хотя бы одной точки в домене и знака @ в email. Возвращает True, если email допустимый и False - в противном случае.'''
    # print(email.split(sep = '@')[1])
    if email.count('@') == 1:
        if len(email.split(sep = '@')) > 1 and '.' in email.split(sep = '@')[-1]: return True
        else: return False
    else: return False

def request_info():
    '''Requests info from CLI and returns dict()'''
    print('Please, input user info')
    f_name = input('Input First name: ')
    l_name = input('Input Last name: ')
    email = input('Input email: ')
    id = str(uuid.uuid4())
    if valid_email(email):
        one_user = {'id': id,
                    'first_name': f_name,
                    "last_name": l_name,
                    "email": email
                    }
        return one_user
    else:
        print('Invalid email, please try again')
        return False

def main():
    '''Interact with stdin\stdout.
    '''
    print('Read all user data')
    users = read(JSON_USER_FILE)
    mode = input('Which mode do you prefer? (1 - find user | 2 - add user) ')
    if mode == '1':
        who = input('Please, input user\'s name: ')
        if find(who, users): print('User has founded')
        else: print('No this user')
    elif mode == '2':
        one_user = request_info()
        if one_user:
            users.append(one_user)
            save(users, JSON_USER_FILE)
            print('User saved to DB')

    else:
        print('Incorrect mode, please choose 1 or 2')
        return
    
    


if __name__ == "__main__":
    main()

