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
        if self.body[idx] == HashTable.__EMPTY:
            self.body[idx] = value
            print(f'key added to position {idx}')
        else:
            # Collision
            # some logic to change idx
            print(f'collision at position {idx}!')


    def delete(self, key):
        idx = self.hasher.hash(key)
        self.body[idx] = HashTable.__EMPTY
