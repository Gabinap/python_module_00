"""
Data Quest - Data Archivist
Exercise 3: Vault Security

This module demonstrates secure file operations using the sacred 'with'
protocol. Ensures automatic vault sealing (file closing) even if errors
occur, implementing the RAII principle for resource management.

Functions:
    main: Demonstrate secure file operations with automatic cleanup

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""


def main() -> None:
    """
    Implements vault security protocols using the 'with' statement.
    Demonstrates secure reading and writing operations with automatic
    resource cleanup, ensuring vaults are properly sealed after use.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    with open("classified_data.txt") as vault:
        for line in vault:
            print(f"[CLASSIFIED] {line.strip()}")

    print()

    print("SECURE PRESERVATION:")
    with open("security_log.txt", "w") as vault:
        vault.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
