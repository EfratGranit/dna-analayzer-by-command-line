class BatchDB(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not BatchDB.__instance:
            BatchDB.__instance = object.__new__(cls)
            self = BatchDB.__instance
            self.__batches = {}
        return BatchDB.__instance

    def add_new_batch(self, name, value):
        self.__batches[name] = value

    def get_by_name(self, name):
        return self.__batches.get(name)

    def get_all(self):
        return self.__batches.keys()
