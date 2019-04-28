"""Use this file for getting functions relating to getting files.

This file contains functions for getting the files in a specified directory along
with subdirectories too.
"""
from glob import glob
from os import getcwd
from typing import Optional


def get_list_of_files(root_path: Optional[str] = None) -> list:
    """Use this function to get a list of all of the files in a directory.

    This function is used for returning a list of files for a given root directory.
    It'll search the root directory along with any sub-directories.

    :param root_path: the root path to search for files in.
    :return: the list of files.
    """
    if not root_path:
        root_path = getcwd()
    return [file for file in glob(f"{root_path}/**/*.py", recursive=True)]
