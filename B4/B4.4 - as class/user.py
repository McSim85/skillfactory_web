#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
It reads user list from json and It asks you about users.
Writes to json-file
'''

import json
import os
import uuid
import time
import datetime

JSON_USER_FILE = 'users.json'
LOG_DATA_FILE_PATH = "last_seen_log.json"

class User():
    '''Read and write info about users'''
    
    def __init__(self, db):
        self.db = db
        self.users = self.read(self.db)
    
    def read(self, filename):
        '''It reads info about users from filemane
        and return list() of dict()s about users.
        filename - str with filename path
        '''
        
        if not os.path.exists(filename) or os.path.getsize(filename) == 0 :
            return []
        
        with open(filename) as db:
            users = json.load(db)
        
        return users

    def save(self, users, filename):
        '''It writes info about users into filename.
        users - list() of dict()s with user info
        filename - str with filename path
        '''
        
        with open(filename, 'w') as db:
            json.dump(users, db)

    def find(self, user):
        '''It find user in DB by name '''
        
        for a_user in self.users:
            if a_user['first_name'] == user: return a_user
            
    def valid_email(self, email):
        '''Проверяет наличие хотя бы одной точки в домене и знака @ в email. Возвращает True, если email допустимый и False - в противном случае.'''
        
        if email.count('@') == 1:
            if len(email.split(sep = '@')) > 1 and '.' in email.split(sep = '@')[-1]: return True
            else: return False
        else: return False

    def request_info(self):
        '''Requests info from CLI and returns dict()'''
        
        print('Please, input user info')
        f_name = input('Input First name: ')
        l_name = input('Input Last name: ')
        email = input('Input email: ')
        id = str(uuid.uuid4())
        if self.valid_email(email):
            one_user = {'id': id,
                        'first_name': f_name,
                        "last_name": l_name,
                        "email": email
                        }
            return one_user
        else:
            print('Invalid email, please try again')
            return False

    def add_user(self, user_data):
        '''Добавляет данные пользователя user_data в список всех пользователей и сохраняет обновленный список '''
        
        self.users.append(user_data)
        self.save(self.users, self.db)

    
class LastSeenLog():
    ''' Get and save user time login '''
    
    def __init__(self, db):
        self.db = db
        self.logs = self.load(self.db)
    
    def load(self, j_db):
        '''Reads info from DB'''
        
        if not os.path.exists(j_db) or os.path.getsize(j_db) == 0 :
            return dict()
        
        with open(j_db) as db:
            logs = json.load(j_db)
        
        return logs

    def save(self, data, json_db):
        '''It saves data to db '''
        
        with open(json_db, 'w') as db:
            json.dump(data, db)
            
    def update_timestamp(self, user_id):
        '''Update info for user_id'''
        ct = time.time()
        self.logs[user_id] = ct
        self.save(self.logs, self.db)

    def find(self, user_id):
        '''It finds timestamp about user_id'''
        if self.logs.get(user_id):
            last_seen_time_stamp = self.logs[user_id]
            last_seen_date_time = datetime.datetime.fromtimestamp(last_seen_time_stamp)
            return last_seen_date_time.isoformat()


def main():
    '''Interact with stdin\stdout.
    '''
    print('Read all user data')
    users = User(JSON_USER_FILE)
    logins = LastSeenLog(LOG_DATA_FILE_PATH)
    mode = input('Which mode do you prefer? (1 - find user | 2 - add user) ')
    if mode == '1':
        who = input('Please, input user\'s name: ')
        if users.find(who): print('User has founded')
        else: print('No this user')
    elif mode == '2':
        one_user = users.request_info()
        if one_user: 
            users.add_user(one_user)
            print(one_user)
            print(one_user['id'])
            logins.update_timestamp(one_user['id'])
        else: print('Invalid user')
    else:
        print('Incorrect mode, please choose 1 or 2')
        return
    
    


if __name__ == "__main__":
    main()

