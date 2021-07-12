from general_func import error


class CDelete:
    def run(self, words, dna):
        if len(words) == 2 and words[1][0] == '#' and len(words[1]) > 1 and dna.get_by_id(int(words[1][1:])):
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
        else:
            error(', should get exist id as second operator')
