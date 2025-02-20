import os

from datadog_checks.dev import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
HOST = get_docker_hostname()

TAGS = [u"foo:bar", u"baz"]

URL = f'http://{HOST}:9600'
PORT = 9600
BAD_PORT = 9405
BAD_URL = f'http://{HOST}:{BAD_PORT}'

GOOD_INSTANCE = {'url': URL, 'tags': TAGS}
BAD_INSTANCE = {'url': BAD_URL}
