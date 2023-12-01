"""

A module for managing configuration using YAML files.

This module provides functions to handle configuration settings for an application.
The primary function, `get_config`, allow users to read a YAML configuration file.
If the specified configuration file does not exist, it creates a new one by copying a default
configuration file. The `get_config_path` is a helper function that locates or creates the
configuration path as necessary.

Functions:
    get_config_path(path=str): Determines the correct path for the configuration file.
        If the provided path does not exist, it first checks if a file with the
        specified name exists in the current directory or in a default directory and
        if necessary, creates the appropriate directories and copies over the default
        configuration file.

    get_config(path=str): Reads and loads the configuration data from a YAML file.
        It utilizes `get_config_path` to ensure that the configuration file is present
        and then loads its contents. If the file doesn't exist, it will be created
        with default settings copied from the default configuration template.

Attributes:
    config_filename (str): Name of the default configuration file.
    user_config_path (str): The full default path to the user configuration file, which is
        determined by joining the default configuration directory and the `config_filename`.

Note: Documentation automatically generated by https://undoc.ai
"""
import os
import shutil
from importlib import resources

import yaml

from .local_storage_path import get_storage_path

config_filename = "config.yaml"

user_config_path = os.path.join(get_storage_path(), config_filename)


def get_config_path(path=user_config_path):
    """
        Retrieves the path to the configuration file, potentially creating it if necessary.
        This function looks for the configuration file in the following order:
        1. Checks if the file exists at the given path.
        2. Checks if the file exists within the application storage path.
        3. Checks if the file exists in the current working directory.
        If the file does not exist in any of those locations, it will:
            a. Attempt to create the directory structure for the provided path, if it includes a directory component that does not exist.
            b. If no directory was specified, or after creating the directory, it will generate the configuration file in the application's default storage path.
        After establishing the appropriate file path but finding no existing file, the function will copy a default configuration file into the determined path.
        Args:
            path (str, optional): The path where the configuration file is expected. Defaults to `user_config_path`.
        Returns:
            str: The absolute path to the configuration file. If the file did not exist, it is created and the path to the new file is returned.
        Raises:
            OSError: If the function cannot create the necessary directories or if copying the default config file fails.
    """
    # check to see if we were given a path that exists
    if not os.path.exists(path):
        # check to see if we were given a filename that exists in the config directory
        if os.path.exists(os.path.join(get_storage_path(), path)):
            path = os.path.join(get_storage_path(), path)
        else:
            # check to see if we were given a filename that exists in the current directory
            if os.path.exists(os.path.join(os.getcwd(), path)):
                path = os.path.join(os.path.curdir, path)
            # if we weren't given a path that exists, we'll create a new file
            else:
                # if the user gave us a path that isn't our default config directory
                # but doesn't already exist, let's create it
                if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                else:
                    # Ensure the user-specific directory exists
                    os.makedirs(get_storage_path(), exist_ok=True)

                    # otherwise, we'll create the file in our default config directory
                    path = os.path.join(get_storage_path(), path)

                # If user's config doesn't exist, copy the default config from the package
                here = os.path.abspath(os.path.dirname(__file__))
                parent_dir = os.path.dirname(here)
                default_config_path = os.path.join(parent_dir, "config.yaml")

                # Copying the file using shutil.copy
                new_file = shutil.copy(default_config_path, path)

    return path


def get_config(path=user_config_path):
    """
    Fetches the configuration from the specified path.
    This function reads the configuration file, expected to be in YAML format, located at the path given by the user or a default path if none is provided. If the path does not exist, it will attempt to generate the configuration by resolving the path using alternative directories such as the storage path or current working directory, or by creating new directories as needed. Finally, it will read and parse the configuration file into a Python dictionary.
    Args:
        path (str, optional): The path to the user's configuration file. If not specified, a default path is used.
    Returns:
        dict: The configuration data parsed from the YAML file.
    """
    path = get_config_path(path)

    with open(path, "r") as file:
        return yaml.safe_load(file)
