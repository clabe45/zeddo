"""
zeddo.config

Read and write configuration file.
"""

import os.path
import click
import toml

CONFIG_PATH = os.path.join(
    click.get_app_dir(app_name='zeddo'),
    'config'
)


def get_config():
    """
    Read configuration file.

    :return: Configuration
    :rtype: dict
    """
    with open(CONFIG_PATH, 'r') as c:
        return toml.load(c)


def set_config(config):
    """
    Write configuration file.

    :param config: Configuration
    :type config: dict
    """
    with open(CONFIG_PATH, 'w+') as c:
        toml.dump(config, c)
