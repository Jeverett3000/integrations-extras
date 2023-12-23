import pytest

from .common import MOCK_INSTANCE_BAD, MOCK_INSTANCE_GOOD


@pytest.fixture(scope='session')
def dd_environment():
    yield {'instances': [MOCK_INSTANCE_BAD, MOCK_INSTANCE_GOOD]}


@pytest.fixture(scope='session')
def good_instance():
    return MOCK_INSTANCE_GOOD.copy()


@pytest.fixture(scope='session')
def bad_instance():
    return MOCK_INSTANCE_BAD.copy()
