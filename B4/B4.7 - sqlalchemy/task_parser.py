#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse_connection_string(connection_string):
    '''
    Принимает на вход строку соединения connection_string и возвращает словарь с ее составными частями
    '''
    final = {'dialect': '',
             'driver': '',
             'username': '',
             'password': '',
             'host': '',
             'port': '',
             'database': ''}
    proto, dbinfo = connection_string.split(sep = '://')
    # parse protocol
#    for dialect in ('sqlite', 'mysql', 'postgresql', 'oracle', 'mssql'):
#        if dialect in proto:
#            final['dialect'] = dialect
    
    if '+' in proto:
        final['dialect'], final['driver'] = proto.split(sep='+')
    else:
        final['dialect'] = proto
    
    if '/' in dbinfo:
        otherinfo, final['database'] = dbinfo.split(sep='/', maxsplit=1)
    else:
        otherinfo = dbinfo

#    print('otherinfo is ', otherinfo)
    if otherinfo:
        if '@' in otherinfo:
            user, host = otherinfo.split(sep='@')
            #parse hostname
            if ':' in host:
                final['host'], final['port'] = host.split(sep=':')
            else:
                final['host'] = host
            #parse username
            if ':' in user:
                final['username'], final['password'] = user.split(sep=':')
            else:
                final['username'] = user  
            
        else:
            if ':' in otherinfo:
                final['username'], final['password'] = otherinfo.split(sep=':')
            else:
                final['username'] = otherinfo
    
#    print(final)
    return final

if __name__ == '__main__':
    print("sqlite:///b4_7.sqlite3")
    parse_connection_string("sqlite:///b4_7.sqlite3")
    print("sqlite:///slash/b4_7.sqlite3")
    parse_connection_string("sqlite:///slash/b4_7.sqlite3")
    print('postgresql+psycopg2://admin:1234@localhost/b4_7')
    parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7")
    print("m2sql://admin:1234/b4_7")
    parse_connection_string("m2sql://admin:1234/b4_7")