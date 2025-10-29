import os
import sys
import subprocess


SCRIPT = os.path.join(os.path.dirname(__file__), "biggest.py")


def run_with_input(data: str) -> str:
    """Run the biggest.py script with given stdin and return stdout as text."""
    completed = subprocess.run(
        [sys.executable, SCRIPT],
        input=data,
        capture_output=True,
        text=True,
        timeout=5,
    )
    # Combine stdout and stderr to help debugging if needed
    return completed.stdout + completed.stderr


def test_a_greater_than_b():
    out = run_with_input("5\n3\n")
    assert "5 är större än 3" in out


def test_b_greater_than_a():
    out = run_with_input("2\n7\n")
    assert "7 är större än 2" in out


def test_equal_values():
    # current behavior treats equal values as the else-branch
    out = run_with_input("4\n4\n")
    assert "4 är större än 4" in out
