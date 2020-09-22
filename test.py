# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:21:35 2020

@author: Faisal Mangi
"""

import json
import itertools
from operator import itemgetter

f = open('source_file_2.json',)

data = json.load(f)


data = sorted(data, key=itemgetter('priority'), reverse=True)


with open("watchers.json", "w") as json:
    for key, value in itertools.groupby(data, key=itemgetter('watchers')):

        for i in value:
            print(key, i.get('name'), file=json)
            
with open("managers.json", "w") as json:
    for key, value in itertools.groupby(data, key=itemgetter('managers')):

        for i in value:
            print(key, i.get('name'), file=json)

    