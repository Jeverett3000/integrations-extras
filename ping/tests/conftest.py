import pytest


@pytest.fixture(scope="session")
def dd_environment(instance):
    yield instance


@pytest.fixture(scope="session")
def instance_response_time():
    return {
        "host": "127.0.0.1",
        "collect_response_time": True,
        "tags": ["response_time:yes"],
    }


@pytest.fixture(scope="session")
def instance():
    return {"host": "127.0.0.1", "tags": ["ping1", "ping2"]}


@pytest.fixture(scope="session")
def instance_ipv6():
    return {
        "host": "0000:0000:0000:0000:0000:0000:0000:0001",
        "tags": ["ping1", "ping2"],
    }


@pytest.fixture(scope="session")
def empty_instance():
    return {}


@pytest.fixture(scope="session")
def incorrect_ip_instance():
    return {"host": "124.0.0.1"}
