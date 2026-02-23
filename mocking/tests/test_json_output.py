from unittest import mock

from mocking.src.Service import get_user_city


@mock.patch("mocking.src.Service.requests.get")
def test_process_user(mock_request_get):
    mock_request_get.return_value = mock.Mock(**{"status_code": 200,
                                                 "json.return_value": [{'name': 'John', 'city': 'NY'},
                                                                       {'name': 'Lily', 'city': 'San Jose'}]})
    output = get_user_city()
    print(output)
