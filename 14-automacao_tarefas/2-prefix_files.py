from pathlib import Path

root_dir = Path('dados')
files_paths = list(root_dir.iterdir())
print(list(files_paths))

for file in files_paths:
    # print(file.stem)
    # print(file.suffix)
    new_filename = f"new-{file.stem}{file.suffix}"
    print(new_filename)
    new_filepath = file.with_name(new_filename)
    file.rename(new_filepath)


