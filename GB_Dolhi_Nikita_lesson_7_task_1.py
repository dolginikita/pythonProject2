# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp


import os

project_path = 'my_project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']

for p in paths:
    os.makedirs(os.path.join(os.curdir, project_path, p), exist_ok=True)

import os

with open('data/config1.yaml', 'r', encoding='utf-8') as ps:
    for_list = [el.strip().split('|--')[-1] for el in ps]
    os.makedirs(for_list[0], exist_ok=True)
    os.chdir(for_list[0])
    for_list.remove(for_list[0])
    for el in for_list:
        os.makedirs(el, exist_ok=True)