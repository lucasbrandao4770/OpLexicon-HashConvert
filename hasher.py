import hashlib


class Hasher():

    def hash(self, key, func_name):
        valid_names = ['md5', 'sha1', 'sha224', 'sha256', 'sha384']
        if func_name in valid_names:
            if func_name == 'md5':
                return self.__md5(key)
            else:
                pass
        pass

    def __md5(self, key):
        pass

    def __sha1(self, key):
        pass

    def __sha224(self, key):
        pass

    def __sha256(self, key):
        pass

    def __sha384(self, key):
        pass
