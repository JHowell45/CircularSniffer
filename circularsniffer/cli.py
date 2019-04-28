"""Use this file for creating the CLI for this package.

This file contains the functions used for creating the CLI for the current package to
allow commands to be executed in a terminal.
"""
from pprint import pprint

import click
from click import Path

from .file_functions import get_list_of_files


@click.group()
def main():
    """CLI for the circular import sniffer application."""
    pass


@main.command()
@click.argument("root_directory", nargs=1, type=Path(exists=True), required=False)
def app_tree(root_directory):
    """Command for listing directory paths for given root.

    This command is used for returning the files for the given root directory passed.
    It will search the subdirectories too if they exist.
    """
    if root_directory:
        python_files = get_list_of_files(root_directory)
    else:
        python_files = get_list_of_files()
    pprint(python_files)


if __name__ == "__main__":
    main()
