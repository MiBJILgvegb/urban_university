from logging import root


def SingleRootWords(root_word,*other_words):
    same_words=[]

    for word in other_words:
        if(root_word.lower() in word.lower())or(word.lower() in root_word.lower()):
            same_words.append(word)

    return same_words

def Main():
    print(SingleRootWords('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
    print(SingleRootWords('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))