# Python-Interactive_Dictionary
# Enter any word and this application will return the definiton. 
# It also accounts for mispelled words and will suggest a similar word

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("/Users/alexandermurrietta/Documents/PythonMasterClass/Python Application Class/Project 1: Dictionary/data.json"))

input_word = input("Please enter a word: ")
lowercase = input_word.lower()

def translate(w):

    if w in data:
        return data.get(lowercase)
    elif w.title() in data:
        return data.get(w.title())
    elif w.upper() in data:
        return data.get(w.upper())
    elif len(get_close_matches(lowercase, data.keys())) > 0:
        yn = input("Did you mean '%s' instead? (Type Y if yes, or N if no): " % get_close_matches(lowercase, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(lowercase, data.keys())[0]]
        elif yn == "N":
            return data.get(lowercase, "That word does not exist. Please double check it.")
        else:
            return "We can't seem to process your request. Please try again."

    else:
        return data.get(lowercase, "That word does not exist. Please double check it.")

output = (translate(lowercase))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
