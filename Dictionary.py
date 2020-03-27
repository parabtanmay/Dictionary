import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word][0]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data: 
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("\nDid you mean %s instead? \nEnter 'Y' for yes and 'N' for No: " % get_close_matches(word,data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn == "N" or yn == "n":
            return "\nThe Word does not exits!\n"

        else:
            return "\nWe Didn't understand your entry!\n"

    else:
        return "\nThe Word does not exist!\n "

while(1):
    word = input("\nEnter a Word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print("\n", item,"\n")
    else:
        print("\n", output,"\n")

