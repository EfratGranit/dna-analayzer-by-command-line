from utils.general_func import find_name
from commands_classes.validate_com.manage_validations import ManValid


class CLoad:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            with open(words[1], 'r') as file:
                new_word = file.read()
                if len(words) == 2:
                    new_word = dna.set(new_word, '@'+find_name(dna, words[1][:words[1].find('.')]))
                else:
                    new_word = dna.set(new_word, words[2])
                print(f'[{new_word["d_id"]}] {new_word["d_name"]}: {new_word["d_con"]}')

