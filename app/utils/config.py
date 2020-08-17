from python_json_config import ConfigBuilder


def get_config():
    builder = ConfigBuilder()
    config = builder.parse_config('config.json')
    return config