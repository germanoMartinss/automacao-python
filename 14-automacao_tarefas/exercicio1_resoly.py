import os

# 1 - Diretório raiz do SO
base_path = os.path.expanduser("~")
print(base_path)

# 2 - Navega diretório downloads
path = os.path.join(base_path, "Downloads")
print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos
files = os.listdir(work_dir)
print(files)

# 4 - Criar pastas 
type_files = ['zip', 'mp4', 'jpeg', 'csv', 'txt', 'py', 'json', 'pdf', 'mp3']

for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)

# 5 - Organizando arquivos

for file in files:
    for type in type_files:
        if '.' + type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)