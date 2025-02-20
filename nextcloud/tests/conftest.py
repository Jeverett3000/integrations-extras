import os
import subprocess
from copy import deepcopy

import pytest

from datadog_checks.dev import WaitFor, docker_run

from .common import BASE_CONFIG, CONTAINER_NAME, HERE, HOST, INVALID_URL, PASSWORD, USER, VALID_URL


@pytest.fixture(scope="session")
def dd_environment():
    """
    Spin up and initialize couchbase
    """

    with docker_run(
        compose_file=os.path.join(HERE, 'compose', CONTAINER_NAME),
        env_vars={'NEXTCLOUD_ADMIN_USER': USER, 'NEXTCLOUD_ADMIN_PASSWORD': PASSWORD},
        conditions=[
            WaitFor(nextcloud_container, attempts=15),
            WaitFor(nextcloud_install, attempts=15),
            WaitFor(nextcloud_add_trusted_domain, attempts=15),
            WaitFor(nextcloud_stats, attempts=15),
        ],
    ):
        yield BASE_CONFIG


@pytest.fixture
def instance():
    return BASE_CONFIG


@pytest.fixture
def empty_url_instance():
    empty_url_instance = deepcopy(BASE_CONFIG)
    empty_url_instance['url'] = ''
    return empty_url_instance


@pytest.fixture
def invalid_url_instance():
    invalid_url_instance = deepcopy(BASE_CONFIG)
    invalid_url_instance['url'] = INVALID_URL
    return invalid_url_instance


def nextcloud_container():
    """
    Wait for nextcloud to start
    """
    status_args = ['docker', 'exec', '--user', 'www-data', CONTAINER_NAME, 'php', 'occ', 'status']
    return subprocess.call(status_args) == 0


def nextcloud_install():
    """
    Wait for nextcloud to install
    """
    status_args = [
        'docker',
        'exec',
        '--user',
        'www-data',
        CONTAINER_NAME,
        'php',
        'occ',
        'maintenance:install',
        '-n',
        f'--admin-user={USER}',
        f'--admin-pass={PASSWORD}',
    ]
    return subprocess.call(status_args) == 0


def nextcloud_add_trusted_domain():
    """
    Wait for nextcloud to add container host to trusted domain
    """
    status_args = [
        'docker',
        'exec',
        '--user',
        'www-data',
        CONTAINER_NAME,
        'php',
        'occ',
        'config:system:set',
        'trusted_domains',
        '2',
        f'--value={HOST}',
    ]
    return subprocess.call(status_args) == 0


def nextcloud_stats():
    """
    Wait for nextcloud monitoring endpoint to be reachable
    """
    status_args = ['curl', '-u', f'{USER}:{PASSWORD}', VALID_URL]
    return subprocess.call(status_args) == 0
