class LocalStorageMock:
    def __init__(self):
        self.store = {}
        self.length = 0


    def key(self, n):
        try:
            return list(self.store.keys())[n]
        except IndexError:
            return None


    def get_item(self, key):
        try:
            return self.store[key]
        except KeyError:
            return None


    def set_item(self, key, value):
        # If the key is empty, the value will not be set
        if key == '' or key is None:
            return 

        self.store[key] = str(value)
        self.length = len(self.store)
        return


    def remove_item(self, key):
        try:
            del self.store[key]
            self.length = len(self.store)
            return
        except KeyError:
            return


    def clear(self):
        self.store = {}
        self.length = 0
        return
