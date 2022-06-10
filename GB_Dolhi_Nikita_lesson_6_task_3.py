from itertools import zip_longest
import json

with open('data/users.csv', 'r', encoding='utf-8') as name, \
        open('data/hobby.csv', 'r', encoding='utf-8') as hobby:
    fio = name.read().splitlines()
    hob = hobby.read().splitlines()

if len(fio) < len(hob):
    print(1)
else:
    fio_hob = dict(zip_longest(fio, hob, fillvalue=None))
    print(fio_hob)
    with open('data/result.txt', 'w', encoding='utf-8') as result:
        json.dump(fio_hob, result, ensure_ascii=False)