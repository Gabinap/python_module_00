

def main():
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        print("Accessing Storage Vault: ancient\\_fragment.txt")
        file = open("ancient_fragment.txt", "r")
        print("connection established...")
        print()
        print("RECOVERDED DATA:")
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