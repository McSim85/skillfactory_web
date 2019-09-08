#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(smth):
    '''Simple return str() + smth '''
    return 'Hello, ' + smth
    
#vat_test = test('Username')

#vat2_test = test()

#print(vat_test)
#
#finc_test = test
#
#finc_test('Test')
#finc_test.name = '444'
#print(finc_test.name)
#test.name = '666'
#print(test.name)
#print(finc_test.name)

def parent(smth):
    
    def child(lang='ru'):
        lang = lang.lower()
        return {'ru': 'Привет, ',
                'en': 'Hello, '}[lang]
    
    final = child() + smth
    return final

print(parent('Dr. Who'))
    

