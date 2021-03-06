import json
import sys

# Method to add a word and it's definition:
def add_word_definition(word, definition):
    add_to_dict = {word: {"definition": f'{definition}', "synonyms": []}}    

    with open("dictionary.json", "r+") as outfile:
        data = json.load(outfile)
        if word not in data:
            data.update(add_to_dict)
            with open("dictionary.json", "w") as outfile:
                json.dump(data, outfile, indent = 2)
        else:
            print('This word with a definition already exists in the dictionary')


# Method to add a word and it's synonym:
def add_word_synonyms(word, synonym):   

    with open("dictionary.json", "r+") as outfile:
        data = json.load(outfile)
        if word in data:
            data[word]['synonyms'].append(synonym)
            with open("dictionary.json", "w") as outfile:
                json.dump(data, outfile, indent = 2)
        else:
            print('This word does not exist in the dictionary')
    

# Method to get a word and it's definition:
def get_word_def(word):
    with open("dictionary.json", "r") as outfile:
        data = json.load(outfile)
        if word in data:
            print(f'{word}:{data[word]["definition"]}')
            return f'{word}:{data[word]["definition"]}'
        else:
            print('That word is not in the dictionary')
            return 'That word is not in the dictionary'


# Method to add a word and it's synonyms:
def get_word_synonyms(word):
    with open("dictionary.json", "r") as outfile:
        data = json.load(outfile)
        if word in data:
            if len(data[word]['synonyms']) > 0:
                print(f'{word}:{data[word]["synonyms"]}')
                return f'{word}:{data[word]["synonyms"]}'
            else:
                print('No synonyms')
                return 'No synonyms'
        else:
            print('That word is not in the dictionary')
            return 'That word is not in the dictionary'


# Command inputs:
if __name__ == "__main__":
    if len(sys.argv) > 1:
    
    # Logic to add the word, split the word and the definition and input appropriate values into the add_word_definition function
        commands = sys.argv[1]
        eachCommand = commands.split(':')

        if len(eachCommand) > 2:
            action = eachCommand[0]
            each_word = eachCommand[1]
            to_add = eachCommand[2]
        else:            
            action = eachCommand[0]
            each_word = eachCommand[1]


        if action == 'addWord':
            add_word_definition(each_word, to_add)

        # Logic to add the synonym, split up the word and the synonym and input the appropriate values into the add_word_synonym function
        if action == 'addSynonym':
            add_word_synonyms(each_word, to_add)
            
        # Logic to get the word definition, get the word from input use the get_word_def function to look up definition
        if action == 'lookupWord':
            get_word_def(each_word)

        # Logic to get the word synonyms, get the word from input use the get_word_synonyms function to get list of synonyms for that word
        if action == 'lookupSynonyms':
            get_word_synonyms(each_word)