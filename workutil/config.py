import os.path as op
import configparser


DEFAULT_PATH = op.expanduser("~/.workutil/")
CONFIG_FILENAME = "config.ini"
MAP_SECTION = "MAP"
API_KEY = "API_KEY"
HOME_ID = "HOME_ID"
WORK_ID = "WORK_ID"


def read_api_file(file_path):
    with open(file_path) as f:
        api = f.read().rstrip()
    return api


class WorkUtilConfig(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(op.join(DEFAULT_PATH, CONFIG_FILENAME))


if __name__ == '__main__':
    wuc = WorkUtilConfig()
