from general_func import error, find_name, allowed
from general_validate import fix_con
from manage_validations import ManValid


class CReplace:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            rep_word = dna.get_by_name(words[1][1:])
            if words[-2] == ':':
                res = fix_con(rep_word['d_con'].get_seq(), words[:-2])
                if words[-1] == '@@':
                    new_word = dna.set(res, '@'+find_name(dna, rep_word['d_name'], '_r'))
                else:
                    new_word = dna.set(res, '@'+find_name(dna, words[-1][1:]))
            else:
                res = fix_con(rep_word['d_con'].get_seq(), words)
                dna.remove_by_id(rep_word['d_id'])
                new_word = dna.set_by_id(res, '@'+rep_word['d_name'], rep_word['d_id'])
            print(f'[{new_word["d_id"]}] {new_word["d_name"]}: {new_word["d_con"]}')



