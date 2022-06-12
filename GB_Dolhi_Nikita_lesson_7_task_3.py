import os
import shutil

way = r'my_project\templates'
for root, dir, files in os.walk('my_project'):
    print(root, dir, files)
    if root == way:
        break
    for file in files:
        print(file, files)
        if file.rsplit('.', 1)[-1].lower() == 'html':
            os.makedirs(os.path.join(way, root.split('\\')[-1]), exist_ok=True)
            print(way, root.split('\\')[-1])
            shutil.copyfile(os.path.join(root, file), os.path.join(way, root.split('\\')[-1], file))