from commands_classes.validate_com.general_validate import val_id
from commands_classes.validate_com.manage_validations import ManValid


class CFind:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            if val_id(words[2], dna):
                word, sub = dna.get_by_id(int(words[1][1:])), dna.get_by_id(int(words[2][1:]))['d_con'].get_seq()
            else:
                word, sub = dna.get_by_id(int(words[1][1:])), words[2]
            print(word['d_con'].get_seq().find(sub))
