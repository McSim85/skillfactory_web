#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import bottle

@bottle.route('/words')
def word_printer():
    words = ['one', 'two', 'three', 'four', 'five']
    for word in words:
        yield f'Here: {word}\n'
        time.sleep(2)


if __name__ == "__main__":
    bottle.run(server='gunicorn')
    #    bottle.run(port=9999)

#to test, use:
# http --stream localhost:9999/words

