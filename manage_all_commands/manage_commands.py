from commands_classes.batch.com_create import CCreate
from commands_classes.batch.com_run import CRun
from commands_classes.batch.com_batchlist import CBatchList
from manage_all_commands.manage_com_batch import ManCommandB


class ManCommand(ManCommandB):
    def __init__(self):
        """Factory Method"""
        super().__init__()
        self._commands.update({
            "batch": CCreate,
            "run": CRun,
            "batchlist": CBatchList
        })

    def find_c(self, command):
        return self._commands[command]()
