from unittest import mock

from mocking.src import Service


@mock.patch("mocking.src.Service.check_availability")
def test_first_mock(first_mock):
    first_mock.return_value = False
    print(Service.is_available())
