#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def word_printer():
    words = ['one', 'two', 'three', 'four', 'five']
    for word in words:
        yield word
        time.sleep(2)

for w in word_printer():
    print(w)


