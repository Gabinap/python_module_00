"""Part IV: Circular Curse Breaking Demonstration."""

from alchemy.grimoire import record_spell, validate_ingredients


def test_ingredient_validation() -> None:
    """Test the ingredient validation system."""
    print("Testing ingredient validation:")
    result1 = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {result1}')
    result2 = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {result2}')
    print()


def test_spell_recording() -> None:
    """Test spell recording with validation."""
    print("Testing spell recording with validation:")
    result1 = record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {result1}')
    result2 = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {result2}')
    print()


def test_late_import_technique() -> None:
    """Demonstrate that late imports avoid circular dependencies."""
    print("Testing late import technique:")
    result = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {result}')
    print()
    print("Circular dependency curse avoided using late imports!")


def main() -> None:
    """Run all demonstrations."""
    print("=== Circular Curse Breaking ===\n")
    test_ingredient_validation()
    test_spell_recording()
    test_late_import_technique()
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
