"""Use this file for creating the CLI for this package.

This file contains the functions used for creating the CLI for the current package to
allow commands to be executed in a terminal.
"""
import click


@click.group()
def main():
    """CLI for the circular import sniffer application."""
    pass


if __name__ == "__main__":
    main()
