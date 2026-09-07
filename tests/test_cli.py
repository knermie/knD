"""Check the installed package's command-line behavior."""

import subprocess
import sys


def test_cli(tmp_path):
    result = subprocess.run(
        [sys.executable, "-m", "knd"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "knD is running.\n"
    assert result.stderr == ""
