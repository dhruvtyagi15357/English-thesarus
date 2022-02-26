import json
import difflib

data = json.load(open("data.json"))

def translate(word):
    lowerword = word.lower()
    upperword = word.upper()
    if lowerword in data:
        return data[lowerword]
    elif upperword in data:
        return data[upperword]
    elif word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        suggestion = difflib.get_close_matches(word, data.keys())[0]
        yn = input("Word \"" + word + "\" doesn't exist. Did you mean " + suggestion + " instead? (Y = Yes, N = No)")
        if yn.lower() == 'y':
            return data[suggestion]
        else:
            return "Unable to understand your query."
    else:
        return "Word doesn't exist. Please check the spelling of the word."

if __name__ == "__main__":
    word = input("Enter the word:")
    result = translate(word)
    if isinstance(result, list):
        for i in range(len(result)):
            print(i+1, ".) ", result[i])
    else:
        print(result)
     
    input("")
