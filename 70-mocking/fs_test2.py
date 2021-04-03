import fs
from unittest import mock

# Run unitest with pytest 'pytest -v fs_test2.py'
@mock.patch('fs.listwd', return_value=b'foo\nbar\n')
def test_listwd(mock_check_output):
    actual_result = fs.listwd()
    expected_directory = b'foo'
    assert expected_directory in actual_result
