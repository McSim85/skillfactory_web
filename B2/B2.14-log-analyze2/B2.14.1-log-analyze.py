#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' timestamp время события, POSIX-like timestamp в миллисекундах
referer поле со ссылкой на страницу, с которой пользователь пришёл на данную страницу интернет магазина
location адрес текущей страницы, на которой произошло событие
party_id уникальный идентификатор пользователя
sessionId уникальный идентификатор сессии
pageViewId уникальный идентификатор текущего просмотра страницы
eventType тип события
item_id id товара
item_price цена
item_url ссылка на товар
dietectedDuplicate булевый флаг-индикатор от системы аналитики, что это сообщение дубль
detectedCorruption булевый флаг-индикатор от системы аналитики, что это сообщение испорчено и его не надо рассматривать
firstInSession булевый флаг, показывающий, что это первое в сессии событие
userAgentName браузер клиента


Вопрос 1. Сколькими браузерами пользуются наши клиенты? 

Для ответа на этот вопрос нужно подсчитать количество уникальных значений поля userAgentName.

Вопрос 2. Какова общая сумма всех покупок? 

Тут нам необходимо вычислить сумму значений поля item_price, для тех событий, у которых поле eventType равно itemBuyEvent
Для расчета всех перечисленных показателей необходимо брать только уникальные — поле detectedDuplicate ложно — и неиспорченные — поле detectedCorruption ложно — записи.
Итак, просматривается следующая логика обработки журналов:
прочитать файл по строкам;
десериализовать строку в словарь, используя метод json.loads;
провести необходимую фильтрацию событий: проверить, что поле detectedDuplicate равно False, поле detectedCorruption равно False, провести дополнительную фильтрацию, необходимую по каждому из пунктов;
провести вычисления;
вывести полученные результаты на экран.
'''

import collections
import json
from pprint import pprint

SRC_500 = 'data_500.json'
SRC_3000 = 'data_3000.json'

raw_500_f = open(SRC_500, mode='r', encoding='utf-8')
list_500 = [json.loads(string) for string in raw_500_f]
#for a_dict in list_500:
#    print(a_dict['userAgentName'])
#pprint(list_500[1:3])
raw_500_f.close()

raw_3000_f = open(SRC_3000, mode='r', encoding='utf-8')
list_3000 = [json.loads(string) for string in raw_3000_f]
raw_3000_f.close()

#user_agents = set(agent['userAgentName'] for agent in list_500
#                  if agent['detectedDuplicate'] == False
#                  and agent['detectedCorruption'] == False )
##pprint(user_agents)
#print(f'Number of user agents for {list_500}: ', len(user_agents))
#
#sum_purchases = sum(agent['item_price'] for agent in list_500
#                    if agent['eventType'] == 'itemBuyEvent'
#                    and agent['detectedDuplicate'] == False
#                    and agent['detectedCorruption'] == False)
#print(f'Number of user agents for {list_500}: ', sum_purchases)



for lst in [list_500, list_3000]:
    user_agents = set()
    sum_purchases = int()
    likes = collections.Counter()
    for agent in lst:
        if agent['detectedDuplicate'] == False and agent['detectedCorruption'] == False:
            user_agents.add(agent['userAgentName'])
            if agent['eventType'] == 'itemBuyEvent':
                sum_purchases += int(agent['item_price'])
            '''
В журнале журнал 2 есть события с типом itemFavEvent (поле eventType равно itemFavEvent).
Они появились после того, как в наш интернет-магазин добавили возможность внести товар в
    избранное (то есть пользователь может товар пометить "звёздочкой" или "лайкнуть").
    Модифицируйте программу для построения следующих метрик по избранным товарам:

Популярность нововведения. Посчитайте, сколько товаров было добавлено в избранное.
Количество звёздочек для каждого товара. То есть, сколько раз товар был добавлен в избранное для каждого из товаров.
Для того, чтобы различать товары используйте идентификатор в поле item_id — он уникален для каждого товара.
По сути, вам надо рассчитать в программе количество звёздочек для каждого такого идентификатора. 
            '''
            if agent['eventType'] == 'itemFavEvent':
                likes[agent['item_id']] += 1
                
    print('Number of user agents for: ', len(user_agents))
    print('Number of user agents for: ', sum_purchases)
    
print('Number of Favorite items: ', len(likes))
print('item_id which wasliked  1359 times: ', ''.join(i for i, v  in likes.items() if v == 1359))    
print('Most popular item: ', likes.most_common(1))
print('Most UNpopular item: ', likes.most_common()[-1])
    
    


    
    
    