"""
Data Quest - Data Archivist
Exercise 4: Crisis Response

This module demonstrates comprehensive crisis management for archive
operations. Implements a generic crisis handler that manages different
types of archive access failures using try/except combined with the
with statement to prevent data corruption.

Functions:
    crisis_handler: Generic function to handle archive access with error management
    main: Test crisis response with various archive scenarios

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""


def crisis_handler(archive_name):
    """
    Generic crisis handler for archive operations.
    Attempts to access an archive and handles all potential failures
    gracefully using secure protocols.
    
    Args:
        archive_name (str): Name of the archive to access
        
    Returns:
        tuple: (success: bool, message: str, status: str)
    """
    try:
        with open(archive_name, "r") as vault:
            content = vault.read().strip()
            return (
                True,
                f"Archive recovered - \"{content}\"",
                "Normal operations resumed"
            )
            
    except FileNotFoundError:
        return (
            False,
            "Archive not found in storage matrix",
            "Crisis handled, system stable"
        )
        
    except PermissionError:
        return (
            False,
            "Security protocols deny access",
            "Crisis handled, security maintained"
        )
        
    except IsADirectoryError:
        return (
            False,
            "Target is a directory, not an archive",
            "Crisis handled, system stable"
        )
        
    except OSError as e:
        return (
            False,
            f"System error: {e.strerror}",
            "Crisis handled, system recovering"
        )
        
    except Exception as e:
        return (
            False,
            f"Unexpected anomaly: {type(e).__name__}",
            "Crisis handled, diagnostics complete"
        )


def main():
    """
    Tests the crisis response system with various archive scenarios.
    Demonstrates proper error handling and system stability.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    
    test_scenarios = [
        ("lost_archive.txt", "CRISIS ALERT"),
        ("classified_vault.txt", "CRISIS ALERT"),
        ("standard_archive.txt", "ROUTINE ACCESS")
    ]
    
    for archive, alert_type in test_scenarios:
        print(f"{alert_type}: Attempting access to '{archive}'...")
        
        success, message, status = crisis_handler(archive)
        
        if success:
            print(f"SUCCESS: {message}")
        else:
            print(f"RESPONSE: {message}")
        
        print(f"STATUS: {status}")
        print()
    
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()