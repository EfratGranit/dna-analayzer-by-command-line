from class_dna import DnaSequence


class ManDna(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not ManDna.__instance:
            ManDna.__instance = object.__new__(cls)
            self = ManDna.__instance
            self._dna_seqs = {}
            self.__id = {}
            self._id_dna = 1
            self._name_dna = 1
        return ManDna.__instance

    def set(self, value, name=None):
        self._id_dna += 1
        return self.set_by_id(value, name, self._id_dna-1)

    def get_by_name(self, name, default=None):
        return self._dna_seqs.get(name, default)

    def get_by_id(self, id, default=None):
        return self._dna_seqs.get(self.__id.get(id, default), default)

    def remove_by_id(self, id):
        name = self.__id[id]
        self.__id.pop(id)
        self._dna_seqs.pop(name)
        
    def set_by_id(self, value, name, id):
        if name:   # if name exist or empty, return None - error
            if self._dna_seqs.get(name[1:]) or name[0] != '@' or len(name) < 2:
                return None
            word = {'d_id': id, 'd_name': name[1:], 'd_con': DnaSequence(value)}
        else:   # adds with inbuilt name, after a check that name doesnt exist
            while self._dna_seqs.get('seq'+str(self._name_dna)):
                self._name_dna += 1
            word = {'d_id': id, 'd_name': 'seq'+str(self._name_dna), 'd_con': DnaSequence(value)}
            self._name_dna += 1
        self._dna_seqs[word['d_name']] = word
        self.__id[word['d_id']] = word['d_name']
        return word
