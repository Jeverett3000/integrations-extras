import os

import pytest

from datadog_checks.dev import docker_run, get_docker_hostname, get_here

URL = f'http://{get_docker_hostname()}:8181'
PROMETHEUS_URL = f"{URL}/metrics"
INSTANCE = {'opa_url': URL, 'prometheus_url': PROMETHEUS_URL}


@pytest.fixture(scope='session')
def dd_environment():
    compose_file = os.path.join(get_here(), 'docker-compose.yml')
    with docker_run(compose_file, endpoints=[URL]):
        yield


@pytest.fixture
def instance():
    return INSTANCE.copy()
