from commands_classes.validate_com.manage_validations import ManValid


class CLen:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            word = dna.get_by_id(int(words[1][1:]))
            print(len(word['d_con']))
