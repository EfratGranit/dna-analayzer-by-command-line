from manage_all_commands.command_interface import CommandRun, Invoker
from dna.manage_dna import ManDna
from utils.config import commands
from utils.general_func import error
from manage_all_commands.manage_commands import ManCommand


if __name__ == '__main__':
    man_com = ManCommand()
    dna = ManDna()
    while True:
        com = input('> cmd >>>')
        words = com.split()
        if len(words) < 1:
            error('enter any command')
        elif words[0] in commands:
            receiver = man_com.find_c(words[0])
            cmd = CommandRun(receiver)
            invoker = Invoker()
            invoker.command(cmd)
            invoker.execute(words, dna)
        else:
            error()
