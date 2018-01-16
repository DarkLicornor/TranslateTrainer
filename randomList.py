#!/usr/bin/env python
# -*- coding: utf-8 -*-
from animals import *
from sentences import *
from food import *
from adjectives import *
from verbs import *
from nature import *
from house import *
from clothes import *
from peopleFamily import *
from questions import *
from numbers import *
from money import *
from food import *

import random


allList = {}
allList.update(animals)
allList.update(sentences)
allList.update(food)
allList.update(adjectives)
allList.update(verbs)
allList.update(nature)
allList.update(house)
allList.update(clothes)
allList.update(peopleFamily)
allList.update(questions)
allList.update(numbers)
allList.update(money)
allList.update(food)

randomList = {}

for i in range(20):
    randomKey = random.choice(list(allList))
    randomList[randomKey] = allList[randomKey]
