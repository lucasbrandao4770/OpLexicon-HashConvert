from utils.hasher import Hasher

class HashTable():
    __EMPTY = None
    def __init__(self, size=42209, hashing_func='md5') -> None:
        self.size = size
        self.hasher = Hasher(table_size=size, hashing_func=hashing_func)
        self.body = [self.__EMPTY]*size
        self.n_keys = 0


    def add(self, key, value):
        idx = self.hasher.hash(key)

        while (self.body[idx] != HashTable.__EMPTY):
            if self.body[idx] == value:
                return
            idx = self.__handle_collision(idx)

        self.body[idx] = value
        self.n_keys += 1


    def delete(self, key):
        idx = self.hasher.hash(key)
        self.body[idx] = HashTable.__EMPTY


    def __setitem__(self, key, value):
        self.add(key, value)


    def get(self, key, value):
        idx = self.hasher.hash(key)
        while self.body[idx]!=value and self.body[idx]!=HashTable.__EMPTY:
            idx = self.__handle_collision(idx)

        return self.body[idx]


    def __handle_collision(self, idx):
        return (idx+1) % self.size
