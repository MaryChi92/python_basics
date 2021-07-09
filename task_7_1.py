import os

root_folder = 'my_project_1'
subfolders = ['settings', 'mainapp', 'adminapp', 'authapp']
for subf in subfolders:
    dir_path = os.path.join(root_folder, subf)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
