from abc import ABC


class Command(ABC):
    """constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver

    """execute method"""
    def execute(self, words, dna):
        pass


class CommandRun(Command):
    """constructor method"""
    def __init__(self, receiver):
        super().__init__(receiver)

    """execute method"""
    def execute(self, words, dna):
        self.receiver.run(words, dna)


class Invoker:
    def __init__(self):
        self.__cmd = None

    """command method"""
    def command(self, cmd):
        self.__cmd = cmd

    """execute method"""
    def execute(self, words, dna):
        self.__cmd.execute(words, dna)
