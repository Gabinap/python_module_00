"""Part I: Sacred Scroll Mastery Demonstration."""

import alchemy
import alchemy.elements


def test_direct_module_access() -> None:
    """Test accessing functions directly through the module."""
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
    )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
    )
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    print()


def test_package_level_access() -> None:
    """
    Test accessing functions at package level (controlled by __init__.py).
    """
    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()


def test_package_metadata() -> None:
    """Test accessing package metadata from __init__.py."""
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


def main() -> None:
    """Run all demonstrations."""
    print("=== Sacred Scroll Mastery ===\n")
    test_direct_module_access()
    test_package_level_access()
    test_package_metadata()


if __name__ == "__main__":
    main()
