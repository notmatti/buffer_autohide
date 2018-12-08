"""
Class to mock the weechat functionality
"""

"""Callback return value"""
WEECHAT_RC_OK = 'OK'
"""Emulate scripts.conf as a simple dictionary"""
config = {}


def config_is_set_plugin(config_name):
    return config_name in config.keys()


def config_set_plugin(config_name, value):
    config[config_name] = value


def config_get_plugin(config_name):
    return config[config_name]


def config_unset_plugin(config_name):
    del(config[config_name])


# We don't care about the rest
def config_set_desc_plugin(option, description):
    return None


def infolist_get(arg1, arg2, arg3):
    return None


def infolist_pointer(arg1):
    return None


def infolist_next(arg1):
    return None


def infolist_free(arg1):
    return None


def current_buffer(arg1):
    return None


def buffer_get_string(arg1, arg2):
    return None


def infolist_integer(arg1):
    return None


def buffer_set(arg1, arg2, arg3):
    return None


def info_get_hashtable(arg1, arg2):
    return None


def info_get(arg1, arg2):
    return None

def prnt(arg1, arg2):
    return ""
