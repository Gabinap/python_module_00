"""
Data Quest - Data Archivist
Exercise 0: Ancient Text Recovery

This module demonstrates basic file reading operations for recovering
data from ancient archives. Showcases file opening, reading, error
handling, and proper file closing.

Functions:
    main: Read and display contents from ancient_fragment.txt

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""


def main() -> None:
    """
    Read and display contents from 'ancient_fragment.txt'.

    Attempts to open and print the file contents. Handles common file
    access errors and reports user-friendly messages.
    """
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        print("Accessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        for line in file:
            print(line, end="")
        file.close()
        print()
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("Error: Storage Vault 'ancient_fragment.txt' not found.")
    except PermissionError:
        print("Error: Access to Storage Vault denied.")
    except IsADirectoryError:
        print("Error: Expected a file but found a directory.")
    except OSError as e:
        print(f"OS Error: {e.strerror}")
    except MemoryError:
        print("Error: Insufficient memory to complete the operation.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
