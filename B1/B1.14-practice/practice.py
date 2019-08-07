#!/usr/bin/env python3
# -*- coding: utf-8 -*-

flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

# выше были данные, а после этой строчки
# вам надо дописать код.

sepal_length = list()
#for _, params in flowers.items():
#    for param, values in params.items():
#        if param == "sepal_length":
#            sepal_length = sepal_length + values
#            
#            #print(sepal_length)
# КОРОЧЕ
for flower, params in flowers.items():
    sepal_length += params["sepal_length"]
    
# ЕЩЕ КОРОЧЕ
for itemses in flowers.values():
    print(itemses["sepal_length"])

## общее среднее значение для sepal_length:
mean_sepal_length = sum(sepal_length) / len(sepal_length)
#print(mean_sepal_length)

# ЕЩЕ ЕЩЕ короче и непонятней
mean_sepal_length2 = sum([i for itemses in flowers.values() for i in itemses["sepal_length"] ]) / len([i for itemses in flowers.values() for i in itemses["sepal_length"] ])
print(mean_sepal_length2)

# общее среднее значение для sepal_width:
mean_sepal_width = sum([i for itemses in flowers.values() for i in itemses["sepal_width"] ]) / len([i for itemses in flowers.values() for i in itemses["sepal_width"] ])
print(mean_sepal_width)
# общее среднее значение для petal_length:
mean_petal_length = sum([i for itemses in flowers.values() for i in itemses["petal_length"] ]) / len([i for itemses in flowers.values() for i in itemses["petal_length"] ])
print(mean_petal_length)