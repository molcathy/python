import pytest
from unittest import mock
import line_reader

@pytest.fixture()
def mockopen(monkeypatch):
    mockfile = mock.MagicMock()
    mockfile.readline = mock.MagicMock(return_value="test line")

    mockopen = mock.MagicMock(return_value=mockfile)
    monkeypatch.setattr("builtins.open", mockopen)
    return mockopen

def test_returnsCorrectString(mockopen, monkeypatch):
    mock_exists = mock.MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = line_reader.read_from_file("blah")
    mockopen.assert_called_once_with("blah", "r")
    assert result == "test line"

def test_throwsExceptionWithBadFile(mockopen, monkeypatch):
    mock_exists = mock.MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with pytest.raises(Exception):
        result = line_reader.read_from_file("blah")
