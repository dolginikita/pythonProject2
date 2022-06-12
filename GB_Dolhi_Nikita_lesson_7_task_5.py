import os
import json

folder = 'some_files'
size_dict = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        key_dict = os.stat(os.path.join(root, file)).st_size // 10 * 10 + 10
        f_ext = file.rsplit('.')[-1]
        if key_dict in size_dict:
            size_dict[key_dict][1].append(f_ext)
            size_dict[key_dict] = (size_dict[key_dict][0] + 1, list(set(size_dict[key_dict][1])))
        else:
            size_dict.setdefault(key_dict, (1, [f_ext]))

res_d = {k: size_dict[k] for k in sorted(size_dict.keys())}
print(res_d)
with open('data/result.json', 'w') as f:
    json.dump(res_d, f)

with open('data/result.json', 'r') as f:
    print(json.load(f))