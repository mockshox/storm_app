from python_json_config import ConfigBuilder

import os


def get_config():
    builder = ConfigBuilder()
    config = builder.parse_config('config.json')
    return config