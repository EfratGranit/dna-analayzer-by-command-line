from commands_classes.batch.batch_db import BatchDB


class CBatchList:
    def run(self, words, dna):
        b_commands = BatchDB()
        for item in b_commands.get_all():
            print(item, end=" ")
        print()
