import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_file(path):
    content = False
    cwd = os.getcwd()
    path = '/'.join([cwd, path])
    with open(path, 'r') as data:
        try:
            content = json.load(data)
        except Exception as e:
            logger.exception(e)
    return content


def handler():
    spec = get_file('src/specs/event_specification.json')
    logger.info(json.dumps(spec))

