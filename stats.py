def get_num_words(contents):
    num_words = len(contents.split())
    
    return num_words

import string
def get_num_letters(text):
    # convert everything to lowercase
    text = text.lower()
    mydict = {}

    for i in string.ascii_lowercase:
        mydict[i] = text.count(i)

    return mydict

def sort_on(items):
    return items["num"]

def get_sorted_num_letters(dictcount):
    mylist = []

    for i in dictcount:
        mylist.append({"char": i, "num": dictcount[i]})

    mylist.sort(reverse=True, key=sort_on)

    return mylist

