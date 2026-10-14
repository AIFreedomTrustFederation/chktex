"""Regression contract for the checked-in autotools bootstrap script.

Uses stub autotools to exercise exit propagation without modifying a real build.
Run: python3 -m unittest discover -s tests -p 'test_autogen_fail_closed.py' -v
"""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "autogen.sh"
TOOLS = ("aclocal", "autoheader", "automake", "autoconf")


class AutogenExitTests(unittest.TestCase):
    def run_bootstrap(self, failing_tool=None):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bindir = root / "bin"
            bindir.mkdir()
            log = root / "calls"
            stub = '''#!/bin/sh
case " $* " in *" --version "*) exit 0;; esac
printf '%s\\n' "${0##*/}" >> "$CALL_LOG"
if [ "${0##*/}" = "$FAIL_TOOL" ]; then exit 23; fi
exit 0
'''
            for tool in TOOLS:
                path = bindir / tool
                path.write_text(stub)
                path.chmod(0o755)
            env = dict(os.environ, PATH=f"{bindir}:{os.environ.get('PATH', '')}",
                       CALL_LOG=str(log), FAIL_TOOL=failing_tool or "")
            result = subprocess.run(["sh", str(SCRIPT)], cwd=root, env=env,
                                    text=True, capture_output=True)
            calls = log.read_text().splitlines() if log.exists() else []
            return result, calls

    def test_success_runs_all_four_tools(self):
        result, calls = self.run_bootstrap()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(calls, list(TOOLS))

    def test_failed_aclocal_stops_bootstrap(self):
        result, calls = self.run_bootstrap("aclocal")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, ["aclocal"])

    def test_failed_autoheader_stops_bootstrap(self):
        result, calls = self.run_bootstrap("autoheader")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, ["aclocal", "autoheader"])

    def test_failed_automake_stops_bootstrap(self):
        result, calls = self.run_bootstrap("automake")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, ["aclocal", "autoheader", "automake"])

    def test_failed_autoconf_stops_bootstrap(self):
        result, calls = self.run_bootstrap("autoconf")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, list(TOOLS))


if __name__ == "__main__":
    unittest.main()
