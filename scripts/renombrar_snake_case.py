import os
import re

def to_snake_case(name):
    # Convierte nombres como InterfaceUserDAO → interface_user_dao
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower()

def rename_project_files_and_folders(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        # Renombrar archivos
        for filename in filenames:
            if filename.endswith('.py'):
                new_name = to_snake_case(filename)
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_name)
                if new_name != filename:
                    os.rename(old_path, new_path)
                    print(f'Renamed file: {filename} → {new_name}')

        # Renombrar carpetas
        for dirname in dirnames:
            new_name = to_snake_case(dirname)
            old_path = os.path.join(dirpath, dirname)
            new_path = os.path.join(dirpath, new_name)
            if new_name != dirname:
                os.rename(old_path, new_path)
                print(f'Renamed folder: {dirname} → {new_name}')

# 👇 Cambia esta ruta a la raíz de tu proyecto
project_root = "/ruta/a/tu/proyecto"
rename_project_files_and_folders(project_root)
