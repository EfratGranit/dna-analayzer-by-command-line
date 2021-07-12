import json
from general_func import error
from config import ending


class CSave:
    def run(self, words, dna):
        if 1 < len(words) < 4 and len(words[1]) > 1 and dna.get_by_name(words[1]):
            save_word = dna.get_by_name(words[1]).copy()
            save_word.update({'d_con': save_word['d_con'].get_seq()})
            if len(words) == 2:
                with open(words[1]+ending, 'w') as file:
                    file.writelines(json.dumps(save_word))
            else:
                with open(words[2] + ending, 'w') as file:
                    file.writelines(json.dumps(save_word))
            print("Saved successfully")
        else:
            error(', should get exist id with # before as second operator')
