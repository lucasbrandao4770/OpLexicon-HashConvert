from utils.hasher import Hasher
import numpy as np

class HashTable():
    _EMPTY = None
    def __init__(self, size=42209, hashing_func='md5') -> None:
        self.size = size
        self.hasher = Hasher(table_size=size, hashing_func=hashing_func)
        self.body = [self._EMPTY]*size
        self.n_keys = 0
        self._probe_seq = np.random.RandomState(seed=42).permutation(self.size)
        self._collision_idx = -1


    def add(self, key, value):
        idx = self.hasher.hash(key)

        while (self.body[idx] != HashTable._EMPTY):
            if self.body[idx] == value:
                return
            idx = self._handle_collision(idx)

        self._reset_collision_idx()
        self.body[idx] = value
        self.n_keys += 1


    def delete(self, key):
        idx = self.hasher.hash(key)
        self.body[idx] = HashTable._EMPTY


    def get(self, key, value):
        idx = self.hasher.hash(key)

        while self.body[idx]!=value and self.body[idx]!=HashTable._EMPTY:
            idx = self._handle_collision(idx)

        self._reset_collision_idx()
        return self.body[idx]


    def _handle_collision(self, idx):
        self._collision_idx += 1
        return (idx + self._probe_seq[self._collision_idx]) % self.size


    def _reset_collision_idx(self):
        self._collision_idx = -1


    def __setitem__(self, key, value):
        self.add(key, value)
