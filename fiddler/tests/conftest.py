import os

import pytest

from datadog_checks.dev import docker_run, get_docker_hostname, get_here

URL = f'http://{get_docker_hostname()}:9000'
FIDDLER_API_KEY = 'eSZ7iyuywmODU0ftl1GvqzuxLNE8mxFWovBftInhqY4'
INSTANCE = {"url": "https://demo.fiddler.ai", "fiddler_api_key": FIDDLER_API_KEY, "organization": "demo"}


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(get_here(), 'docker-compose.yml')

    # This does 3 things:
    #
    # 1. Spins up the services defined in the compose file
    # 2. Waits for the url to be available before running the tests
    # 3. Tears down the services when the tests are finished
    with docker_run(compose_file, endpoints=[URL], build=True):
        yield instance


@pytest.fixture
def instance():
    return INSTANCE.copy()
