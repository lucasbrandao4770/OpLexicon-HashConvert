import hashlib


class Hasher():
    def __init__(self, table_size=42) -> None:
        self.table_size = table_size

    def hash(self, key, func_name='md5'):
        valid_names = ['md5', 'sha1', 'sha224', 'sha256', 'sha384']

        assert func_name in valid_names, f"Please enter a valid hashing function. \
                                            Valid functions are: {valid_names}\n"

        hash_func = getattr(hashlib, f'{func_name}')
        hashed_value = hash_func(key.encode('utf-8')).hexdigest()
        return self.__transform(hashed_value)


    def __transform(self, key):
        return (sum([ord(c) for c in key])**2) % self.table_size
