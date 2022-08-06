import json
from difflib import get_close_matches

#loading json file
data = json.load(open("dictionary.json"))

def translate(w):
    #convert to lower case
    w = w.lower()

    if w in data:
        return data[w]
    #for getting close match of the word
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("Did you mean % s instead?Entry Y if yes and N if no" %get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist."
        else:
            return "We didn't understand."
    else:
        return "The word doesn't exist.DO check the spelling."
work = input("Please enter your word: ")
output = translate(work)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
    input("Press ENTER to exit.")


        

