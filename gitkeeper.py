import os, sys

KEEP_FILE_NAME = ".gitkeep"
CURRENT_DIR = os.getcwd()
MODE = sys.argv[1] if len(sys.argv) > 1 else '' # 'add' or 'del' arg


def find_empty_dirs(dir):
    paths = []
    for dirpath, dirs, files in os.walk(dir):
        if not dirs and not files and '.git' not in dirpath:
            paths.append(dirpath)
    return paths


def add_keep_files(paths):
    for path in paths:
        open(os.path.join(path, KEEP_FILE_NAME),"w+")
    return len(paths)


def find_not_empty_dirs(dir):
    paths = []
    for dirpath, dirs, files in os.walk(dir):
        if (dirs or files) and '.git' not in dirpath and KEEP_FILE_NAME in files:
            paths.append(dirpath)
    return paths


def delete_keep_files(paths):
    for path in paths:
        os.remove(os.path.join(path, KEEP_FILE_NAME))
    return len(paths)


print("\ngitkeeper running...")
if MODE.lower() == 'add':
    print(f'Adding {KEEP_FILE_NAME} files recursively to empty subdirectories of the current directory...')
    count = add_keep_files(find_empty_dirs(CURRENT_DIR))
    print(f'Added {count} {KEEP_FILE_NAME} files!\n')
elif MODE.lower() == 'del':
    print(f'Deleting {KEEP_FILE_NAME} files from not empty directories...')
    count = delete_keep_files(find_not_empty_dirs(CURRENT_DIR))
    print(f'Deleted {count} {KEEP_FILE_NAME} files!\n')
else:
    print('Mode argument is not valid!\nPlease provide "add" or "del" as first argument!\n')
