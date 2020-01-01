# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:03:47 2019

@author: Aman Singh
"""
import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes or enter N if no." %get_close_matches(word,data.keys())[0])
        yn=yn.upper()
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exit.Try another word.Thank You"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exit.Try another word.Thank You"

word=input("Enter word you want to search:")
output=translate(word)


if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)


