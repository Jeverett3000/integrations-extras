import os

from datadog_checks.dev.docker import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(HERE, "docker")
HOST = get_docker_hostname()
URL = f'http://{HOST}:5066'
ENDPOINT = f'{URL}/stats'
FIXTURE_DIR = os.path.join(HERE, "fixtures")
BAD_ENDPOINT = f'http://{HOST}:1234/stats'


def registry_file_path(name):
    return os.path.join(FIXTURE_DIR, f"{name}_registry.json")
