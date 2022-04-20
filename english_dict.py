import json
from difflib import get_close_matches

data= json.load(open("G:\PYTHON PROJECTS1\DICTIONARY1\data.json"))

def meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif (len(get_close_matches(word,data))>0):
        temp_output=input("Do you mean %s instead of %s? 'Y' for yes 'N' for no : "%(get_close_matches(word,data)[0],word))
        if (temp_output=="Y" or temp_output=='y'):
            return data[get_close_matches(word,data)[0]]
        elif temp_output=="n" or temp_output=='N':
            return "Sorry word not found. Please crosscheck"
        else:
            return "You have entered a wrong option. Please double-check"
    else:
        return "Word not found.Please double-check"
input_word=input("Hello GARV.Enter the word whose meaning you want to search:")
output=meaning(input_word)
c=0
if type(output)==list:
    for i in output:
        c=c+1
        print(str(c)+".)"+i)
else:
    print(output)

