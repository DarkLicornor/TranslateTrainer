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
from randomList import *
from food import *

####MAIN####
correct = 0
exit = False

choices = [
'Animals',
'Sentences',
'Food',
'Adjectives',
'Verbs',
'Nature',
'House',
'Clothes',
'People & Family',
'Questions',
'Numbers',
'Money',
'Random set of 20 words'
]

choicesCorrespondance = {
1: animals,
2: sentences,
3: food,
4: adjectives,
5: verbs,
6: nature,
7: house,
8: clothes,
9: peopleFamily,
10: questions,
11: numbers,
12: money,
13: randomList,
}

while(not exit):
    ### Chose theme to learn ###
    print ("What do you want to learn ? \n (type q to exit) \n")
    for i in range(len(choices)):
        print (str(i+1) +") "+ choices[i]+"\n")
    choice = input()

    ### Select right list depending on user choice ###
    dictToIterateIn = {}
    if choice == 'q':
        exit = True
    else:
        for key, value in choicesCorrespondance.items():
            if int(choice) == key:
                print ("debug" + str(key))
                dictToIterateIn = value

        ### Iterate in chosen dicts ###
        if dictToIterateIn != {}:
            for french, german in dictToIterateIn.items():
                userEntry = input("Translate " + french + " : ")
                if(userEntry == german):
                    print ("_____\n")
                    correct +=1
                else:
                    print ("Correct answer was " + german + "\n_____\n")

            print ("Score : " + str(correct) + "/" + str(len(dictToIterateIn)))
