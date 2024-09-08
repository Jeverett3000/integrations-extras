import pytest

from .common import HOST, PORT


@pytest.fixture
def instance():
    return {
        'url': f'http://{HOST}:{PORT}',
        'api_user': 'foo',
        'password': 'bar',
        'tags': ['foo:bar'],
    }
