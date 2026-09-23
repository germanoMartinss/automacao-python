from pathlib import Path
from datetime import datetime

root_dir = Path(__file__).parent

for path in root_dir.glob("dados*/**/*"):
    if path.is_file():
        stats = path.stat()
        second_created = stats.st_mtime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime("%d-%m-%Y_%H-%M-%S")
        # print(f"{path} foi criado em {date_created_str}")
        new_filename = f"{date_created_str}_{path.name}"
        # print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
