#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###def test(smth):
###    '''Simple return str() + smth '''
###    return 'Hello, ' + smth
###    
####vat_test = test('Username')
###
####vat2_test = test()
###
####print(vat_test)
####
####finc_test = test
####
####finc_test('Test')
####finc_test.name = '444'
####print(finc_test.name)
####test.name = '666'
####print(test.name)
####print(finc_test.name)
###
###def parent(smth):
###    
###    def child(lang='ru'):
###        lang = lang.lower()
###        return {'ru': 'Привет, ',
###                'en': 'Hello, '}[lang]
###    
###    final = child() + smth
###    return final
###
###print(parent('Dr. Who'))
##
##import random
##
##def hello(who):
##    return 'Hello ' + who
##
##def action(name_list, some_func):
##    rand_name = random.choice(name_list)
##    return some_func(rand_name)
##
##print(action(['aaa','bbb','ccc'], hello))
##print(action(['aaa','bbb','ccc'], str))
##print(action(['aaa','bbb','ccc'], print))
#
#def parent(who):
#    def child():
#        #it used who from parent
#        return 'Hello, ' + who
#    # Same child() may be lambda:
##    child = lambda: 'Hello, ' + who
#    
#    return child
#    
#var_parent = parent('Dr. Who')
#print(var_parent())

''' Допустим, мы хотим получить h2 заголовок внутри div с классом "container".
Для этого модифицируем нашу функцию decorate следующим образом:'''

def compose_hello_func(name):
    get_intro = lambda: "Привет, " + name + "!"
    return get_intro


def decorate(tag, klass=None):
    if klass:
        wrap = lambda text: "<{0} class='{2}'>{1}</{0}>".format(tag, text, klass)
    else:
        wrap = lambda text: "<{0}>{1}</{0}>".format(tag, text)
    return wrap

greeting = compose_hello_func("Арсений")
#print(greeting())

print(decorate("div", "container")
      (decorate("H2")
       (greeting())
       )
      )
