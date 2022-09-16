from utils.hasher import Hasher

class HashTable():
    def __init__(self, size=42209, hasher=None) -> None:
        self.size = size
        if hasher is None:
            self.hasher = Hasher(size)
