# To be run like this:
#   python3 -m pytest -v test/test_rpi_ac_control.py
#   python3 -m pytest -k 'test_run_shell_cmd' -v test/test_rpi_ac_control.py

import pytest
import os
import re
from test_utils.io import *
from test_utils.systemd import *
from test_utils.shell import *


@pytest.mark.parametrize(
    'directory', ["/opt/rpi-ac-control", "/var/log/rpi-ac-control"])
def test_directories_exist(directory):
    assert is_dir(directory)


@pytest.mark.parametrize(
    'file', ["/opt/rpi-ac-control/tbd.py", "/var/log/rpi-ac-control/tbd"])
def test_files_exist(file):
    assert is_file(file)
    assert os.path.getsize(file) > 0
