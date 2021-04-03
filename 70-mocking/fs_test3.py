import fs
import pytest
import subprocess
from unittest import mock

# Run unitest with pytest 'pytest -v fs_test3.py'
def test_listwd(monkeypatch):
    # Create your own replacement for the actual subprocess.check_output
    # Note it has to take an argument same as the original subprocess.check_output
    def mock_subchout(command):
        print(command)
        return b'foo\nbar\n'

    # Replace subprocess.check_output with your own command
    monkeypatch.setattr(subprocess, 'check_output', mock_subchout)

    assert b'foo' in fs.listwd()
