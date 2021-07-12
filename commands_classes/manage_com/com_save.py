from utils.config import ending
from commands_classes.validate_com.specific_validations import val_save


class CSave:
    def run(self, words, dna):
        if val_save(dna, words):
            save_word = dna.get_by_name(words[1][1:]).copy()
            save_word.update({'d_con': save_word['d_con'].get_seq()})
            if len(words) == 2:
                with open(words[1][1:]+ending, 'w') as file:
                    file.writelines(save_word['d_con'])
            else:
                with open(words[2] + ending, 'w') as file:
                    file.writelines(save_word['d_con'])
            print("Saved successfully")
