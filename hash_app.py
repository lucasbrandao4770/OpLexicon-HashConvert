"""Main class

Responsável pela execução da aplicação.
"""

from utils.hash_table import HashTable
from utils.hash_table_timer import HashTableTimer

with open('base_de_dados.txt', 'r') as file:
    data = file.readlines()
functions = ['md5', 'sha1', 'sha224', 'sha256', 'sha512']
times = {}
for func_name in functions:
    table = HashTableTimer(hasher = func_name)
    for line in data:
        line = line.split(sep=',')
        table[line[0]] = line
        table.get(line[0], line)

    times[func_name] = {
        "Number of collisions": table.n_collisions,
        "Mean search time": table.search_time["total"]/table.search_time["count"],
        "Mean hashing time": table.hash_time["total"]/table.hash_time["count"],
    }

print(times)
