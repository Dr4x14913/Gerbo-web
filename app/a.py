#! /usr/bin/python3
def filter_string(string):
    illegal_char_map = {
            "e": ['é', 'è', 'ë'],
            "a": ['à'],
            "": ["'", "%", "$", "*"]
            }
    string = string.lower()
    for letter, illegal in illegal_char_map.items():
        for c in illegal:
            string = string.replace(c,letter)

    # replace any blanck spaces more than 1 by one
    return " ".join(string.split())
