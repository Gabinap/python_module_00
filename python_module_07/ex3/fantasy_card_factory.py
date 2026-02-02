"""
DataDeck - Exercise 3: Game Engine
FantasyCardFactory Implementation

This module implements a concrete card factory that creates
fantasy-themed cards (dragons, goblins, fireballs, magic rings, etc).

Classes:
    FantasyCardFactory: Concrete factory for fantasy cards

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

import random
from typing import Any

from ex0.card import Card
from ex0.creature_card import CreatureCard
from ex1.artifact_card import ArtifactCard
from ex1.spell_card import SpellCard

from ex3.card_factory import CardFactory


class FantasyCardFactory(CardFactory):
    """
    Fantasy-themed card factory.

    Creates cards with fantasy theme:
    - Creatures: Dragons, Goblins, Elves, Orcs
    - Spells: Fireball, Ice Lance, Lightning Bolt
    - Artifacts: Mana Ring, Magic Staff, Crystal Orb

    Attributes:
        _creature_templates: Dictionary of creature definitions
        _spell_templates: Dictionary of spell definitions
        _artifact_templates: Dictionary of artifact definitions

    Methods:
        create_creature: Create fantasy creatures
        create_spell: Create elemental spells
        create_artifact: Create magical artifacts
        create_themed_deck: Build balanced fantasy deck
        get_supported_types: List all available card types
    """

    def __init__(self) -> None:
        """Initialize factory with fantasy card templates."""

        self._creature_templates: dict[str, dict[str, Any]] = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 7,
                "rarity": "Legendary",
                "attack": 7,
                "health": 7,
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 2,
            },
            "elf": {
                "name": "Forest Elf",
                "cost": 3,
                "rarity": "Uncommon",
                "attack": 2,
                "health": 3,
            },
            "orc": {
                "name": "Orc Berserker",
                "cost": 4,
                "rarity": "Common",
                "attack": 4,
                "health": 3,
            },
        }

        self._spell_templates: dict[str, dict[str, Any]] = {
            "fireball": {
                "name": "Fireball",
                "cost": 4,
                "rarity": "Common",
                "effect_type": "damage",
            },
            "ice_lance": {
                "name": "Ice Lance",
                "cost": 2,
                "rarity": "Common",
                "effect_type": "damage",
            },
            "healing": {
                "name": "Healing Touch",
                "cost": 3,
                "rarity": "Uncommon",
                "effect_type": "heal",
            },
            "lightning": {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": "Rare",
                "effect_type": "damage",
            },
        }

        self._artifact_templates: dict[str, dict[str, Any]] = {
            "mana_ring": {
                "name": "Mana Ring",
                "cost": 2,
                "rarity": "Uncommon",
                "durability": 5,
                "effect": "+1 mana per turn",
            },
            "magic_staff": {
                "name": "Magic Staff",
                "cost": 4,
                "rarity": "Rare",
                "durability": 3,
                "effect": "+2 spell power",
            },
            "crystal": {
                "name": "Crystal Orb",
                "cost": 3,
                "rarity": "Rare",
                "durability": 4,
                "effect": "Scry 2 cards",
            },
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy creature card.

        Args:
            name_or_power: Creature name ("dragon", "goblin", etc),
                          power level (int), or None for random

        Returns:
            CreatureCard with fantasy theme

        Examples:
            create_creature("dragon")
            create_creature(5)
            create_creature()
        """

        if isinstance(name_or_power, int):
            power = name_or_power

            for key, template in self._creature_templates.items():
                if template["cost"] == power:
                    name_or_power = key
                    break
                if template["cost"] > power:
                    name_or_power = key
                    break

        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._creature_templates:
                template = self._creature_templates[template_key]
            else:
                template = self._creature_templates["goblin"]
        else:
            template = random.choice(list(self._creature_templates.values()))

        return CreatureCard(
            name=template["name"],
            cost=template["cost"],
            rarity=template["rarity"],
            attack=template["attack"],
            health=template["health"],
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy spell card.

        Args:
            name_or_power: Spell name ("fireball", etc),
                          power level (int), or None for random

        Returns:
            SpellCard with fantasy theme
        """

        if isinstance(name_or_power, int):
            power = name_or_power
            for key, template in self._spell_templates.items():
                if template["cost"] == power:
                    name_or_power = key
                    break
                if template["cost"] > power:
                    name_or_power = key
                    break

        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._spell_templates:
                template = self._spell_templates[template_key]
            else:
                template = self._spell_templates["fireball"]
        else:
            template = random.choice(list(self._spell_templates.values()))

        return SpellCard(
            name=template["name"],
            cost=template["cost"],
            rarity=template["rarity"],
            effect_type=template["effect_type"],
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a fantasy artifact card.

        Args:
            name_or_power: Artifact name ("mana_ring", etc),
                          power level (int), or None for random

        Returns:
            ArtifactCard with fantasy theme
        """

        if isinstance(name_or_power, int):
            power = name_or_power
            for key, template in self._artifact_templates.items():
                if template["cost"] == power:
                    name_or_power = key
                    break
                if template["cost"] > power:
                    name_or_power = key
                    break

        if isinstance(name_or_power, str):
            template_key = name_or_power.lower()
            if template_key in self._artifact_templates:
                template = self._artifact_templates[template_key]
            else:
                template = self._artifact_templates["mana_ring"]
        else:
            template = random.choice(list(self._artifact_templates.values()))

        return ArtifactCard(
            name=template["name"],
            cost=template["cost"],
            rarity=template["rarity"],
            durability=template["durability"],
            effect=template["effect"],
        )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Create a balanced fantasy-themed deck.

        Creates a deck with typical fantasy distribution:
        - 50% creatures
        - 30% spells
        - 20% artifacts

        Args:
            size: Total number of cards

        Returns:
            Dictionary with deck information:
                - cards: List of Card objects
                - theme: "Fantasy"
                - size: Total cards
                - composition: Breakdown by type

        Raises:
            ValueError: If size is not positive
        """
        if size <= 0:
            raise ValueError("Deck size must be positive")

        cards = []

        num_creatures = int(size * 0.5)
        num_spells = int(size * 0.3)
        num_artifacts = size - num_creatures - num_spells

        for _ in range(num_creatures):
            cards.append(self.create_creature())

        for _ in range(num_spells):
            cards.append(self.create_spell())

        for _ in range(num_artifacts):
            cards.append(self.create_artifact())

        return {
            "cards": cards,
            "theme": "Fantasy",
            "size": len(cards),
            "composition": {
                "creatures": num_creatures,
                "spells": num_spells,
                "artifacts": num_artifacts,
            },
        }

    def get_supported_types(self) -> dict[str, Any]:
        """
        List all fantasy card types available.

        Returns:
            Dictionary of available card types and variants:
                - creatures: List of creature names
                - spells: List of spell names
                - artifacts: List of artifact names
        """
        return {
            "creatures": list(self._creature_templates.keys()),
            "spells": list(self._spell_templates.keys()),
            "artifacts": list(self._artifact_templates.keys()),
        }
