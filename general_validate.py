from general_func import allowed
from commands_classes.batch.batch_db import BatchDB


def val_id(ope, dna):
    return ope[0] == '#' and len(ope) > 1 and ope[1:].isnumeric() and dna.get_by_id(int(ope[1:]))


def val_exist_empty_name(ope, dna):
    return ope[0] == '@' and len(ope) > 1 and not dna.get_by_name(ope[1:])


def find_name(ope, dna):
    return ope[0] == '@' and len(ope) > 1 and dna.get_by_name(ope[1:])


# return true if words is finished with valid manipulation
def val_manipulate(words, dna):
    if words[-2] == ':':
        if words[-1] == '@@' or val_exist_empty_name(words[-1], dna):
            return True
    return False


def val_int(i, j, _id, dna):
    if -1 < i < j < len(dna.get_by_id(_id)['d_con'])+1:
        return True
    return False


def fix_con(con, words):
    repl_i, repl_v = words[2::2], words[3::2]
    if all(i.isnumeric() for i in repl_i) and all(int(i) < len(con) for i in repl_i) and all(allowed(v) for v in repl_v):
        for i in range(len(repl_i)):
            con = con[:int(repl_i[i])] + repl_v[i] + con[int(repl_i[i])+1:]
        return con
    return None


def val_not_exist_batch(b_name):
    b_point = BatchDB()
    if b_point.get_by_name(b_name):
        return False
    return True

