"""
Data Quest - Data Archivist
Exercise 2: Stream Management

This module demonstrates the three sacred data channels of communication:
stdin for input, stdout for standard output, and stderr for alerts.
Showcases proper stream separation for different message types.

Functions:
    main: Demonstrate proper use of stdin, stdout, and stderr

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""

import sys


def main() -> None:
    """
    Demonstrates the three sacred communication channels of the Archives.
    Collects user input via stdin and routes messages to appropriate streams:
    - sys.stdout for standard messages
    - sys.stderr for alerts and diagnostics
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print()

    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print()

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
