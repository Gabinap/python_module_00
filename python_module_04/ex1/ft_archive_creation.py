def main():
    """
    Simulates the creation of a new archive file in a cyber archive system.
    It writes predefined entries to a new file and handles potential errors.
    exceptions handled include PermissionError, OSError, MemoryError, and a general Exception catch-all.
    """
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print()
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")
        print()

        entries = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee"
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
