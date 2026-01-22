"""
Data Quest - Data Archivist
Exercise 1: Archive Creation

This module demonstrates basic file writing operations for creating
new archive entries. Showcases file creation, writing, error
handling, and proper file closing.

Functions:
    main: Create new_discovery.txt and write archive entries

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""


def main() -> None:
    """
    Simulates the creation of a new archive file in a cyber archive system.
    It writes predefined entries to a new file and handles potential errors.
    Exceptions handled include PermissionError, OSError, and MemoryError.
    A general Exception catch-all is also present.
    """
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print()
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")
        print()

        print("Inscribing preservation data...")
        entries = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee",
        ]
        for entry in entries:
            file.write(entry + "\n")
            print(entry)
        file.close()

        print()
        print("Data inscription complete. Storage unit sealed.\n")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("Error: Access to Storage Vault denied.")
    except OSError as e:
        print(f"OS Error: {e.strerror}")
    except MemoryError:
        print("Error: Insufficient memory to complete the operation.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
