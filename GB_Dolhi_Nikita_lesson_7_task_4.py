import os

folder = 'some_files'
dictonary = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key = 10 ** len(str(size))
        if key in dictonary:
            dictonary[key] += 1
        else:
            dictonary[key] = 1

for key, val in dictonary.items():
    print(f'{key} : {val}')