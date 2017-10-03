from datetime import datetime
import json


def parse_datetime(str_):
    try:
        return datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None


def _merge(base, increment):
    for key, value in increment.items():
        is_dict = type(value) == dict
        base[key] = _merge(base.get(key, {}), value) if is_dict else value
    return base


class ConfigHandler(object):
    def __init__(self, config_path, open, exists):
        self.config_path = config_path
        self.open = open
        self.exists = exists

    def load(self, defaults={}):
        config = defaults
        if self.exists(self.config_path):
            with self.open(self.config_path, 'r') as f:
                try:
                    loaded = json.loads(f.read())
                    config = _merge(config, loaded)
                except Exception:
                    pass
        return config

    def update(self, values):
        config = self.load({})
        config = _merge(config, values)
        with self.open(self.config_path, 'w+') as f:
            f.write(json.dumps(config))


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
