from general_func import error, allowed
from general_validate import val_id, val_manipulate, val_exist_empty_name, val_int, fix_con, find_name, val_not_exist_batch


def val_dup(dna, words):
    if len(words) > 1 and val_id(words[1], dna):  # validate second operator
        if len(words) > 2 and val_exist_empty_name(words[2], dna):  # validate third operator if exist
            return True
        elif len(words) == 2:  # no third operator
            return True
        else:  # if the third is not valid
            error(', attribute name is empty or not unique')
            return False
    error(', should get exist #id then @new_name or nothing')
    return False


def val_load(dna, words):
    try:  # validate existence of file
        with open(words[1], 'r') as file:  # validate the content
            new_word = file.read()
            if not new_word or not allowed(new_word):
                error(',file content is not dna-valid (C T A G)')
                return False
            elif len(words) == 2:  # case two operators
                return True
            elif len(words) == 3 and val_exist_empty_name(words[2], dna):  # third operator case
                return True
            error('enter two or three operators, and third is @new_name - not empty, not exist')
            return False
    except FileNotFoundError:
        error(',enter valid path of existence file')
        return False


def val_new(dna, words):
    if len(words) == 2 and allowed(words[1]):  # validate case two operators
        return True
    elif len(words) == 3 and val_exist_empty_name(words[2], dna):  # case three operators
        return True
    elif len(words) == 3:
        error(',attribute name is empty or not unique not of @new_name kind')
    elif len(words) == 2:
        error(',enter a valid dna sequence')
    else:
        error(', enter 2 or three operators')
    return False


def val_len(dna, words):
    if 2 == len(words) and val_id(words[1], dna):
        return True
    error(', should get exist id with # before as second operator')
    return False


def val_find(dna, words):
    if 3 == len(words) and val_id(words[1], dna):
        if allowed(words[2]) or val_id(words[2], dna):
            return True
        else:
            error(',should get exist id or valid dna sequence as third operator')
    else:
        error(',should get three operators')
    return False


def val_slice(dna, words):
    if 3 < len(words) < 7 and val_id(words[1], dna) and val_int(int(words[2]), int(words[3]), int(words[1][1:]), dna):
        if len(words) == 4:
            return True  # validate case of four operators
        elif val_manipulate(words, dna):  # case of six operators
            return True
        else:
            error()
    else:
        error(', should get #id and i1 < i2 < len of dna as valid indexes')
    return False


def val_replace(dna, words):
    if 3 < len(words) and find_name(words[1], dna) and len(words) % 2 == 0:  # validate length and first item
        if val_manipulate(words, dna):
            if fix_con(dna.get_by_name(words[1][1:])['d_con'].get_seq(), words[:-2]):
                return True   # validate having : at the end
            else:
                error('')
        elif fix_con(dna.get_by_name(words[1][1:])['d_con'].get_seq(), words):  # the other option
            return True
        else:
            error('should get : and then @@ or @new_name, or nothing and valid pairs inside')
    else:
        error(', should get exist name and pairs of index and valid char ')


def val_create_batch(dna, words):
    if len(words) == 2 and words[1][0] == '@' and val_not_exist_batch(words[1][1:]):
        return True
    error(', batch name exist or empty')
    return False


def val_run(dna, words):
    if len(words) == 2 and words[1][0] == '@' and not val_not_exist_batch(words[1][1:]):
        return True
    error(', batch name not exist or empty')
    return False


def val_batch_list(dna, words):
    pass
