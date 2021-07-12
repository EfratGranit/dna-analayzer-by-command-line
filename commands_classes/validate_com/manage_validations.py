from commands_classes.validate_com.specific_validations import *


class ManValid:
    def __init__(self, dna, words):
        self.__dna = dna
        self.__words = words

        """Factory Method"""
        self.__commands = {
            "new": val_new,
            "load": val_load,
            "dup": val_dup,
            "slice": val_slice,
            "del": val_del,
            "save": val_save,
            "replace": val_replace,
            "len": val_len,
            "find": val_find,
            "findall": val_find,
            "batch": val_create_batch,
            "run": val_run,
            "batchlist": val_batch_list
        }

    def find_v(self, command):
        return self.__commands[command](self.__dna, self.__words)
