import os
from core.util import basic_io



def get_twitter_key():
    """
    get twitter api key as string
    :return: (str) key
    """
    path_to_keys = os.path.join('config', 'twitter_keys.json')
    keys = basic_io.read_json_to_dict(path_to_keys)
    return keys["api-key"]