from manage_validations import ManValid
from commands_classes.batch.batch_db import BatchDB


class CCreate:
    def run(self, words, dna):
        commands, b_content = BatchDB(), []
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            cur_com = input('> batch >>>')
            while cur_com != 'end':
                b_content.append(cur_com)
                cur_com = input('> batch >>>')
            commands.add_new_batch(words[1][1:], b_content)
