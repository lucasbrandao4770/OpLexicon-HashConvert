from utils.hash_table import HashTable
import time
import numpy as np


class HashTableTimer(HashTable):
    def __init__(self, size=42209, hasher=None) -> None:
        super().__init__(size, hasher)
        self.n_collisions = 0
        self.hash_time = {"total": 0, "count": 0}
        self.search_time = {"total": 0, "count": 0}

    def add(self, key, value):
        start = time.time()
        idx = self.hasher.hash(key)
        end = time.time()
        self.hash_time["total"] += end-start
        self.hash_time["count"] += 1

        while (self.body[idx] != HashTable._EMPTY):
            if self.body[idx] == value:
                print(f'{key} already in table!')
                return
            self.n_collisions += 1
            print(f'{key} caused collision with {self.body[idx]} at position {idx}!')
            idx = self._handle_collision(idx)

        self._collision_idx = -1
        self.body[idx] = value
        self.n_keys += 1

    def get(self, key, value):
        start = time.time()
        idx = self.hasher.hash(key)

        while (self.body[idx]!=value) and (self.body[idx]!=HashTable._EMPTY):
            idx = self._handle_collision(idx)
            
        self._collision_idx = -1
        end = time.time()
        self.search_time["total"] += end-start
        self.search_time["count"] += 1

        return self.body[idx]
