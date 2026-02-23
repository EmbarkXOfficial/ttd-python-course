from unittest import mock
from mocking.src import Service


@mock.patch("mocking.src.Service.check_availability")
def test_first_mock(first_mock):
    first_mock.return_value = False
    # print(Service.is_available())
    first_mock.assert_not_called()


@mock.patch("mocking.src.Service.get_password")
def test_first_mock_1(second_mock):
    second_mock.return_value = "123"
    print(Service.validate_user("aaa", "123"))
    second_mock.assert_called_once_with("aaa")
