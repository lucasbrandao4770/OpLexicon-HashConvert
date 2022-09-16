import hashlib


class Hasher():
    def __init__(self, table_size=42, hashing_func='md5') -> None:
        valid_names = ['md5', 'sha1', 'sha224', 'sha256', 'sha512']
        assert hashing_func in valid_names, f"Please enter a valid hashing function. \
                                            Valid functions are: {valid_names}\n"
        self.table_size = table_size
        self.hashing_func = getattr(hashlib, f'{hashing_func}')

    def hash(self, key):
        try:
            hashed_value = self.hashing_func(key.encode('utf-8')).hexdigest()
        except (AttributeError, TypeError):
            raise AssertionError('Key should be a string')

        return self.__transform(hashed_value)


    def __transform(self, key):
        return (sum([ord(c) for c in key])**2) % self.table_size
