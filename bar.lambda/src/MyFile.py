import json
import logging
import os
import dateutil

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

def some_function():
    return 'bailando'

def handler():
    spec = get_file('src/specs/event_specification.json')
    logger.info(json.dumps(spec))
