from os import path, rename, remove
from shutil import rmtree


def is_file(filepath):
    '''Wrapper for os.path.isfile()

    Parameters
    ---
    filepath: str, the path to the file
    '''

    print(f'testing if {filepath} is a file')
    return path.isfile(filepath)


def is_dir(dirpath):
    '''Wrapper for os.path.isdir()

    Parameters
    ---
    filepath: str, the path to the file
    '''

    print(f'testing if {dirpath} is a directory')
    return path.isdir(dirpath)


def write_to_file(filepath, content, append=True):
    '''Write lines to a file.

    Parameters
    ---
    filepath: str, the file to modify
    content: str/list, the content to write to the file
    append: bool, if false, content will replace the original file content
    '''

    print(f'trying to write {content} into {filepath}')

    if type(content) == str:
        content = list(content)

    access_mode = 'a' if append else 'w'

    with open(filepath, access_mode) as f:
        f.writelines(content)


def move_file(oldpath, newpath):
    '''Move file from old path to new path.

    Parameters
    ---
    oldpath: str, current path of file
    newpath: str, new path of file
    '''

    print(f'moving: {oldpath} => {newpath}')
    try:
        rename(oldpath, newpath)
    except FileNotFoundError as e:
        print(f'{oldpath} not found')
        raise e


def delete_file(filepath):
    '''Deletes a file.

    Parameters
    ---
    filepath: str, file to be deleted
    '''

    print(f'removing {filepath}')
    try:
        remove(filepath)
    except FileNotFoundError as e:
        print(f'{filepath} not found')
        raise e


def delete_dir(dirpath):
    '''Deletes a directory and all of its contents

    Parameters
    ---
    dirpath: str, dir to be deleted
    '''

    print(f'removing directory {dirpath}')
    try:
        rmtree(dirpath)
    except FileNotFoundError as e:
        print(f'{dirpath} not found')
        raise e
