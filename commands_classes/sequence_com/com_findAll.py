import re
from general_validate import val_id
from manage_validations import ManValid


class CFindAll:
    def run(self, words, dna):
        val = ManValid(dna, words)
        if val.find_v(words[0]):
            if val_id(words[2], dna):
                word, sub = dna.get_by_id(int(words[1][1:])), dna.get_by_id(int(words[2][1:]))['d_con'].get_seq()
            else:
                word, sub = dna.get_by_id(int(words[1][1:])), words[2]
            for item in [m.start() for m in re.finditer(f"(?={sub})", word['d_con'].get_seq())]:
                print(item, end=" ")
            print()
