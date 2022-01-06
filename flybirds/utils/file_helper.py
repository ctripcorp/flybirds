# -*- coding: utf-8 -*-
"""
file helper
"""
import json
import os


def store_json_to_file_path(data, path, write_type):
    """
    json save to file
    """
    with open(path, write_type) as fw:
        json.dump(data, fw)


def get_json_from_file_path(path):
    """
    Get the content of the json file and convert it into an object
    """
    f = None
    result = None
    # noinspection PyBroadException
    try:
        f = open(path, "r", encoding="utf-8")
        json_str = f.read().strip()
        result = json.loads(json_str)
    except Exception as e:
        raise e
    finally:
        if f:
            f.close()
    return result


def get_json_from_file(file_name):
    """
    Get the content of the json file and convert it into an object
    """
    f = None
    result = None
    # noinspection PyBroadException
    try:
        f = open(file_name, "r", encoding="utf-8")
        result = json.load(f)
    except Exception as e:
        raise e
    finally:
        if f:
            f.close()
    return result


def create_dirs(path):
    """
    Check and create path
    """
    path = os.path.join(os.getcwd(), path)
    dir_exist = os.path.exists(path)
    if not dir_exist:
        os.makedirs(path)


def create_dirs_path_object(path):
    """
    Check and create path
    """
    dir_exist = os.path.exists(path)
    if not dir_exist:
        os.makedirs(path)
        return True
    else:
        return False


def clear_dirs(path):
    """
    Clear all files and folders under a folder
    """
    path = os.path.join(os.getcwd(), path)
    if os.path.exists(path):
        ls = os.listdir(path)
        for item in ls:
            c_path = os.path.join(path, item)
            if os.path.isdir(c_path):
                clear_dirs(c_path)
                os.rmdir(c_path)
            else:
                os.remove(c_path)


def valid_file_name(o_name):
    """
    Replace the illegal string in the file
    """
    in_valid_chars = "|\\?*<\":>+[]/',"
    for c in in_valid_chars:
        o_name = o_name.replace(c, "_")
    return o_name.replace(" ", "_")


def array_to_file(file_path, str_array):
    """
    Overwrite data in the file,
    if it does not exist, create a new file
    """
    if isinstance(str_array, list) and len(str_array) > 0:
        f = None
        # noinspection PyBroadException
        try:
            f = open(file_path, "w+", encoding="utf-8")
            for str_index in range(len(str_array)):
                f.write(str(str_array[str_index]))
        except Exception as e:
            raise e
        finally:
            if f:
                f.close()


def get_files_from_dir(file_path):
    """
    Recursively get all files from the directory
    """
    files = []
    for main_dir, dirs, file_name_list in os.walk(file_path):
        for file in file_name_list:
            file_path = os.path.join(main_dir, file)
            files.append(file_path)
    return files


def get_paths_from_dir(file_path, dir_name):
    """
    Recursively get all file paths from the directory
    """
    paths = []
    for main_dir, dirs, file_name_list in os.walk(file_path):
        if dir_name is not None and main_dir.find(dir_name) != -1:
            paths.append(main_dir)
    return paths


def replace_file_content(file_path, key, value):
    """
    replace file content
    """
    new_file = ""
    with open(file_path, "r", encoding="utf-8") as f:
        new_file = f.read()
    new_file = new_file.replace(f"%{{{{{key}}}}}", f"{value}")
    # write file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_file)


def update(filename, text):
    content = ""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    content = content + '\n' + text
    # write file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
