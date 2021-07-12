from utils.general_func import find_name
from commands_classes.validate_com.manage_validations import ManValid


class CDup:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            dup_word = dna.get_by_id(int(words[1][1:]))
            if len(words) == 2:
                new_word = dna.set(dup_word['d_con'].get_seq(), '@'+find_name(dna, dup_word['d_name'], '_'))
            else:
                new_word = dna.set(dup_word['d_con'].get_seq(), words[2])
            print(f'[{new_word["d_id"]}] {new_word["d_name"]}: {new_word["d_con"]}')
