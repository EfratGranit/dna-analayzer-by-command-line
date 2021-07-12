from config import allow


# print error message
def error(message=''):
    print("not a valid syntax " + message)


def allowed(s):
    return all(c in allow for c in s)


def shorten_word(word):
    if len(word) > 40:
        return word[:33]+'...'+word[-3:]
    return word


def find_name(dna, word, add=''):
    counter = 1
    update_word = word
    while dna.get_by_name(update_word):
        update_word = word + add + str(counter)
        counter += 1
    return update_word
