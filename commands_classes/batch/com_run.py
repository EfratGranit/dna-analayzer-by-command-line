from commands_classes.validate_com.manage_validations import ManValid
from commands_classes.batch.batch_db import BatchDB
from utils.config import ba_commands
from utils.general_func import error
from manage_all_commands.command_interface import CommandRun, Invoker
from manage_all_commands.manage_com_batch import ManCommandB


class CRun:
    def run(self, words, dna):
        man_com = ManCommandB()
        b_commands, b_content = BatchDB(), []
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            for item in b_commands.get_by_name(words[1][1:]):
                words = item.split()
                if len(words) > 0 and words[0] in ba_commands:
                    receiver = man_com.find_c(words[0])
                    cmd = CommandRun(receiver)
                    invoker = Invoker()
                    invoker.command(cmd)
                    invoker.execute(words, dna)
                else:
                    error(', empty or invalid command')
