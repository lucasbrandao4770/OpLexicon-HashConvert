from utils.hasher import Hasher

class HashTable():
    __EMPTY = None
    def __init__(self, size=42209, hasher=None) -> None:
        self.size = size
        if hasher is None:
            self.hasher = Hasher(size)
        self.body = [self.__EMPTY]*size


    def add(self, key, value):
        idx = self.hasher.hash(key)

        while (self.body[idx] != HashTable.__EMPTY):
            print(f'{key} caused collision with {self.body[idx]} at position {idx}!')
            idx = self.__handle_collision(idx)
            print(f'idx set to {idx}')

        self.body[idx] = value


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
