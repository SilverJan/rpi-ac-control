# To be run like this:
#   python3 -m pytest -v test/test_rpi_ac_control.py
#   python3 -m pytest -k 'test_run_shell_cmd' -v test/test_rpi_ac_control.py

import pytest
import os
import re
from test_utils.io import *
from test_utils.systemd import *
from test_utils.shell import *

ac_control_service = "ac-control.service"


def test_ac_control_service_enabled_running():
    assert is_service_enabled(ac_control_service)
    assert is_service_running(ac_control_service)


def test_ac_control_service_alive():
    (rc, output) = run_in_shell(
        f"curl 0.0.0.0:5000/version")
    assert rc == 200
    assert output == "1.0.0"


@pytest.mark.parametrize(
    'directory', ["/opt/rpi-ac-control", "/var/log/rpi-ac-control"])
def test_directories_exist(directory):
    assert is_dir(directory)


@pytest.mark.parametrize(
    'file', ["/opt/rpi-ac-control/rpi-ac-control.py", "/var/log/rpi-ac-control/ac-control.log"])
def test_files_exist(file):
    assert is_file(file)
    assert os.path.getsize(file) > 0
