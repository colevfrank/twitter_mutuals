import os
from util import basic_io



def get_api_key():
    """
    get twitter api key as string
    :return: (str) key
    """
    path_to_keys = os.path.join('config', 'twitter_keys.json')
    keys = basic_io.read_json_to_dict(path_to_keys)
    return keys["api_key"]


def get_bearer_token():
    """
    get twitter bearer token as a string
    :return: (str) key
    """
    path_to_keys = os.path.join('config', 'twitter_keys.json')
    keys = basic_io.read_json_to_dict(path_to_keys)
    return keys["bearer_token"]