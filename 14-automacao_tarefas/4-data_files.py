from pathlib import Path
from datetime import datetime

path = Path('dados2/teste.txt')
# print(path.stat())

stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
# print(date_created)

date_created_str = date_created.strftime("%d/%m/%Y-%H:%M:%S")
print(date_created_str)