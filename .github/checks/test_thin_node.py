"""Guard the thin-node Git contract without downloading generated products."""

from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[2]


class ThinNodeTests(unittest.TestCase):
    def test_build_engine_is_not_versioned(self):
        tracked = subprocess.check_output(
            ["git", "ls-files", "--stage", "--", "oswm_codebase"],
            cwd=ROOT,
            text=True,
        )
        self.assertEqual(
            tracked, "", "Remove the core gitlink/files; the builder fetches core_ref."
        )

    def test_ephemeral_checkout_is_ignored(self):
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "--quiet", "oswm_codebase/README.md"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
