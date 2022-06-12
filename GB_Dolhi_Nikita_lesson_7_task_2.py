
import os

settings = {}

with open('data/config.yaml', 'r', encoding='utf-8') as f:
    lines = dict(map(str.split, f.readlines()))
    print(lines)

base_dir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, base_dir, k), exist_ok=True)
    print(f'Создан каталог {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, base_dir, k, i), 'w') as f:
            print(f'Создан файл {i}, в каталоге {k} ')