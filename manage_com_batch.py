from commands_classes.create_com.com_new import CNew
from commands_classes.create_com.com_load import CLoad
from commands_classes.manipulate_com.com_slice import CSlice
from commands_classes.create_com.com_dup import CDup
from commands_classes.manage_com.com_delete import CDelete
from commands_classes.manage_com.com_save import CSave
from commands_classes.manipulate_com.com_replace import CReplace
from commands_classes.sequence_com.com_len import CLen
from commands_classes.sequence_com.com_find import CFind
from commands_classes.sequence_com.com_findAll import CFindAll


class ManCommandB:
    def __init__(self):
        """Factory Method"""
        self._commands = {
            "new": CNew,
            "load": CLoad,
            "dup": CDup,
            "slice": CSlice,
            "del": CDelete,
            "save": CSave,
            "replace": CReplace,
            "len": CLen,
            "find": CFind,
            "findall": CFindAll,
        }

    def find_c(self, command):
        return self._commands[command]()
