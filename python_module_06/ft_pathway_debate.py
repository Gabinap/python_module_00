"""Part III: Pathway Debate Mastery Demonstration."""

import alchemy.transmutation


def test_absolute_imports() -> None:
    """Test functions that use absolute imports (from basic.py)."""
    print("Testing Absolute Imports (from basic.py):")
    lead_result = alchemy.transmutation.lead_to_gold()
    stone_result = alchemy.transmutation.stone_to_gem()
    print(f"lead_to_gold(): {lead_result}")
    print(f"stone_to_gem(): {stone_result}")
    print()


def test_relative_imports() -> None:
    """Test functions that use relative imports (from advanced.py)."""
    print("Testing Relative Imports (from advanced.py):")
    philo_result = alchemy.transmutation.philosophers_stone()
    elixir_result = alchemy.transmutation.elixir_of_life()
    print(f"philosophers_stone(): {philo_result}")
    print(f"elixir_of_life(): {elixir_result}")
    print()


def test_package_access() -> None:
    """Test accessing transmutation functions through the package."""
    print("Testing Package Access:")
    lead_result = alchemy.transmutation.lead_to_gold()
    philo_result = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.lead_to_gold(): {lead_result}")
    print(f"alchemy.transmutation.philosophers_stone(): {philo_result}")
    print()


def main() -> None:
    """Run all demonstrations."""
    print("=== Pathway Debate Mastery ===\n")
    test_absolute_imports()
    test_relative_imports()
    test_package_access()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
