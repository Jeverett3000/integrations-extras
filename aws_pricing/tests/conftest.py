import boto3
import pytest

from tests.pricing_client_stubber import PricingClientStubber


@pytest.fixture()
def pricing_client():
    return boto3.client('pricing', region_name='us-east-1')


@pytest.fixture()
def pricing_client_stubber(pricing_client):
    return PricingClientStubber(pricing_client)
