from pathlib import Path

root_dir = Path(__file__).parent
# files_paths = root_dir.iterdir()
# print(list(files_paths))

# for path in files_paths:
#     print(path)
#     for filepath in path.iterdir():
#         print(filepath)

file_paths = root_dir.glob("**/*")
for path in file_paths:
    # print(path)
    if path.is_file():
        # print(path)
        # print(path.parts[-2])
        parent_folder = path.parts[-2]
        new_filename = f"{parent_folder}_{path.name}"
        # print(new_filename)
        path.rename(new_filename)
