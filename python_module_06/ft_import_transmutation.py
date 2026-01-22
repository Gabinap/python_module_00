"""Part II: Import Transmutation Mastery Demonstration."""

# Method 1: Full module import
import alchemy.elements

# Method 2: Specific function import
# Method 4: Multiple imports
from alchemy.elements import create_earth, create_fire, create_water

# Method 3: Aliased import
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion


def demonstrate_method_1() -> None:
    """Demonstrate full module import usage."""
    print("Method 1 - Full module import:")
    result = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {result}")
    print()


def demonstrate_method_2() -> None:
    """Demonstrate specific function import usage."""
    print("Method 2 - Specific function import:")
    result = create_water()
    print(f"create_water(): {result}")
    print()


def demonstrate_method_3() -> None:
    """Demonstrate aliased import usage."""
    print("Method 3 - Aliased import:")
    result = heal()
    print(f"heal(): {result}")
    print()


def demonstrate_method_4() -> None:
    """Demonstrate multiple imports usage."""
    print("Method 4 - Multiple imports:")
    earth_result = create_earth()
    fire_result = create_fire()
    strength_result = strength_potion()
    print(f"create_earth(): {earth_result}")
    print(f"create_fire(): {fire_result}")
    print(f"strength_potion(): {strength_result}")
    print()


def main() -> None:
    """Run all demonstrations."""
    print("=== Import Transmutation Mastery ===\n")
    demonstrate_method_1()
    demonstrate_method_2()
    demonstrate_method_3()
    demonstrate_method_4()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
