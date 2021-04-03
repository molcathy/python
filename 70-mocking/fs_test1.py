from unittest import mock, TestCase
import fs

# Run unitest with 'python3 -m unittest fs_test1.py'
class TestExamples(TestCase):
    @mock.patch('fs.listwd', return_value=b'foo\nbar\n')
    def test_listwd(self, mock_check_output):
        actual_result = fs.listwd()

        expected_directory = b'bar'

        self.assertIn(expected_directory, actual_result)
