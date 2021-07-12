from utils.general_func import find_name
from commands_classes.validate_com.manage_validations import ManValid


class CSlice:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            slice_word = dna.get_by_id(int(words[1][1:]))
            new_con = slice_word['d_con'].get_seq()[int(words[2]):int(words[3])]
            if len(words) == 4:
                dna.remove_by_id(slice_word['d_id'])
                new_word = dna.set_by_id(new_con, '@'+slice_word['d_name'], slice_word['d_id'])
            elif words[5] == '@@':
                new_word = dna.set(new_con, '@'+find_name(dna, slice_word['d_name'], '_s'))
            else:
                new_word = dna.set(new_con, '@'+find_name(dna, words[5][1:]))
            print(f'[{new_word["d_id"]}] {new_word["d_name"]}: {new_word["d_con"]}')
