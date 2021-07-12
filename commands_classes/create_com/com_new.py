from commands_classes.validate_com.manage_validations import ManValid


class CNew:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            if len(words) == 2:
                new_word = dna.set(words[1])
            else:
                new_word = dna.set(words[1], words[2])
            print(f'[{new_word["d_id"]}] {new_word["d_name"]}: {new_word["d_con"]}')
