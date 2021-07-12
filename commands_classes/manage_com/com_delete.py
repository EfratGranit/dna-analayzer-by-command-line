from commands_classes.validate_com.specific_validations import val_del


class CDelete:
    def run(self, words, dna):
        if val_del(dna, words):
            word = dna.get_by_id(int(words[1][1:]))
            print(f'Do you really want to delete {word["d_name"]}: {word["d_con"].get_seq()}?')
            print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            conf = input('> confirm >>>')
            while conf not in ['Y', 'y', 'N', 'n']:
                print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
                conf = input('> confirm >>>')
            if conf in ['Y', 'y']:
                dna.remove_by_id(int(words[1][1:]))
                print(f'Deleted: [{word["d_id"]}] {word["d_name"]}: {word["d_con"].get_seq()}')
            else:
                print('Deleting canceled')