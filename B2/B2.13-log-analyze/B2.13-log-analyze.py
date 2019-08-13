#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

log = open('dummy-access.log')
text = log.readlines()
#print(type(text))
#list_text = text.splitlines()
#print(type(list_text))
#print(text[0])
log.close()
#ipses = collections.defaultdict(int)
ipses = collections.Counter()

for line in text:
    ip = line.split(sep='[')[0].split()[0]
    ipses[ip] += 1

ip1 = '79.136.245.135'
print(f'How much requests from {ip1}?: ', ipses[ip1])
ip2 = '127.0.0.1'
print(f'How much requests from {ip2}?: ', ipses[ip2])
print('Max request counter: ', ipses.most_common(1))
print('Min request counter: ', ipses.most_common()[-1])
print('Average (round) requests number for all clients: ' , round(sum(ipses.values()) / len(ipses.values())))

    
    
    