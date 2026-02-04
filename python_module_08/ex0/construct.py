"""
Exercise 0:
    Entering the Matrix - Virtual Environment Detection.

Author:
    gagulhon (@École 42)

Version:
    1.0 (2025-02-03)
"""

import os
import site
import sys


def detect_virtual_environment() -> bool:
    """
    Detect if the script is running inside a virtual environment.

    Returns:
        bool: True if running in a virtual environment, False otherwise.
    """
    # Check for VIRTUAL_ENV environment variable
    if os.getenv("VIRTUAL_ENV"):
        return True

    # Check if base_prefix differs from prefix (Python 3.3+)
    if hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix:
        return True

    # Check for real_prefix (older virtualenv)
    if hasattr(sys, "real_prefix"):
        return True

    return False


def get_environment_info() -> dict:
    """
    Gather information about the current Python environment.

    Returns:
        dict: Dictionary containing environment information.
    """
    info = {
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0],
        "prefix": sys.prefix,
        "base_prefix": getattr(sys, "base_prefix", sys.prefix),
        "site_packages": site.getsitepackages(),
        "virtual_env": os.getenv("VIRTUAL_ENV"),
    }
    return info


def display_outside_matrix() -> None:
    """Display information when running outside a virtual environment."""
    print("=" * 60)
    print("MATRIX STATUS: You're still plugged in")
    print("=" * 60)
    print()

    info = get_environment_info()
    print(f"Current Python: {info['python_executable']}")
    print("Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()

    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")
    print("=" * 60)


def display_inside_matrix() -> None:
    """Display information when running inside a virtual environment."""
    print("=" * 60)
    print("MATRIX STATUS: Welcome to the construct")
    print("=" * 60)
    print()

    info = get_environment_info()

    # Try to get venv name from VIRTUAL_ENV or from the prefix path
    if info["virtual_env"]:
        venv_name = os.path.basename(info["virtual_env"])
        venv_path = info["virtual_env"]
    else:
        # Extract from sys.prefix if VIRTUAL_ENV is not set
        venv_path = info["prefix"]
        venv_name = os.path.basename(venv_path)

    print(f"Current Python: {info['python_executable']}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()

    print("Package installation path:")
    if info["site_packages"]:
        for path in info["site_packages"]:
            print(f"  {path}")
    print("=" * 60)


def show_environment_comparison() -> None:
    """Show the difference between global and virtual environment paths."""
    info = get_environment_info()

    print("\nEnvironment Details:")
    print(f"  Python Executable: {info['python_executable']}")
    print(f"  Python Version: {info['python_version']}")
    print(f"  Base Prefix: {info['base_prefix']}")
    print(f"  Current Prefix: {info['prefix']}")

    if info["base_prefix"] != info["prefix"]:
        print("  → Virtual environment detected (prefixes differ)")
    else:
        print("  → Global environment (prefixes are the same)")


def main() -> None:
    """Main function to run the environment detection."""
    print("\n=== Entering the Matrix ===\n")

    is_venv = detect_virtual_environment()

    if is_venv:
        display_inside_matrix()
    else:
        display_outside_matrix()

    # Optional: Show detailed comparison
    if "--verbose" in sys.argv or "-v" in sys.argv:
        show_environment_comparison()


if __name__ == "__main__":
    main()
