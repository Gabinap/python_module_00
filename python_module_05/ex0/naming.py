#!/usr/bin/env python3
"""
Exploration Interactive : all(), any(), et Conventions de Nommage Python

Questions abordées :
1. Comment fonctionne all() ?
2. Conventions de nommage : __attr vs _attr vs attr
3. Impact sur l'exécution vs documentation
"""

print("=" * 70)
print("PARTIE 1 : COMPRENDRE all()")
print("=" * 70)

print("\n--- 1.1 : Comportement de Base ---\n")

# all() retourne True si TOUS les éléments sont True
print("Test 1 : all([True, True, True])")
result1 = all([True, True, True])
print(f"Résultat : {result1}")
print("Explication : Tous vrais → True\n")

print("Test 2 : all([True, False, True])")
result2 = all([True, False, True])
print(f"Résultat : {result2}")
print("Explication : Un seul False suffit → False\n")

print("Test 3 : all([False, False, False])")
result3 = all([False, False, False])
print(f"Résultat : {result3}")
print("Explication : Aucun vrai → False\n")

print("Test 4 : all([])")
result4 = all([])
print(f"Résultat : {result4}")
print("Explication : Liste vide → True (convention mathématique)")
print("             C'est le 'vacuous truth' (vérité vacue)\n")


print("\n--- 1.2 : all() avec une List Comprehension ---\n")

# Exemple de NumericProcessor.validate()
data = [1, 2, 3, 4, 5]
print(f"Données : {data}")
print(f"\nCode : all(isinstance(x, (int, float)) for x in data)")
print("\nDéroulement étape par étape :")

for i, x in enumerate(data, 1):
    check = isinstance(x, (int, float))
    print(f"  Étape {i}: isinstance({x}, (int, float)) = {check}")

result = all(isinstance(x, (int, float)) for x in data)
print(f"\nRésultat final : {result}")
print("→ Tous les éléments sont des nombres → True\n")

# Exemple avec un élément invalide
data_invalid = [1, 2, "hello", 4, 5]
print(f"Données invalides : {data_invalid}")
print(f"\nCode : all(isinstance(x, (int, float)) for x in data_invalid)")
print("\nDéroulement étape par étape :")

for i, x in enumerate(data_invalid, 1):
    check = isinstance(x, (int, float))
    print(f"  Étape {i}: isinstance({x}, (int, float)) = {check}")
    if not check:
        print(f"  ⚠️ ARRÊT ! all() s'arrête dès qu'il trouve False")
        break

result = all(isinstance(x, (int, float)) for x in data_invalid)
print(f"\nRésultat final : {result}")
print("→ Un élément n'est pas un nombre → False\n")


print("\n--- 1.3 : all() - Court-circuit (Short-circuit) ---\n")

print("IMPORTANT : all() s'arrête dès qu'il trouve False !")
print("Il ne vérifie PAS tous les éléments si ce n'est pas nécessaire.\n")

def check_with_print(x):
    """Fonction qui affiche quand elle est appelée"""
    print(f"  → Vérification de {x}")
    return x > 0

data_test = [5, 3, -1, 10, 8]
print(f"Données : {data_test}")
print(f"Code : all(check_with_print(x) for x in data_test)\n")

result = all(check_with_print(x) for x in data_test)
print(f"\nRésultat : {result}")
print("\n⚡ Observation : all() s'est arrêté à -1 !")
print("   Il n'a PAS vérifié 10 et 8 → optimisation\n")


print("\n--- 1.4 : Comparaison all() vs any() ---\n")

print("┌─────────────┬──────────────────────────────────────┐")
print("│  Fonction   │           Comportement               │")
print("├─────────────┼──────────────────────────────────────┤")
print("│   all()     │  True si TOUS sont True              │")
print("│             │  False dès qu'un False est trouvé    │")
print("│             │  all([]) → True                      │")
print("├─────────────┼──────────────────────────────────────┤")
print("│   any()     │  True dès qu'un True est trouvé      │")
print("│             │  False si TOUS sont False            │")
print("│             │  any([]) → False                     │")
print("└─────────────┴──────────────────────────────────────┘\n")

# Exemples pratiques
tests = [
    [True, True, True],
    [True, False, True],
    [False, False, False],
    []
]

print("Tests comparatifs :\n")
for test in tests:
    print(f"Liste : {test}")
    print(f"  all() : {all(test)}")
    print(f"  any() : {any(test)}\n")


print("\n--- 1.5 : all() en Action dans NumericProcessor ---\n")

from typing import Any

def validate(data: Any) -> bool:
    """Version simplifiée de NumericProcessor.validate()"""
    print(f"Validation de : {data}")
    print(f"Type : {type(data)}")
    
    # Étape 1 : Est-ce une liste ?
    if not isinstance(data, list):
        print("  ✗ Pas une liste → False")
        return False
    
    print("  ✓ C'est une liste")
    
    # Étape 2 : Tous les éléments sont des nombres ?
    print("  Vérification de chaque élément :")
    result = all(isinstance(x, (int, float)) for x in data)
    
    if result:
        print("  ✓ Tous les éléments sont des nombres → True")
    else:
        print("  ✗ Au moins un élément n'est pas un nombre → False")
    
    return result

# Tests
print("\nTest 1 : Liste valide")
validate([1, 2, 3, 4])

print("\n" + "-" * 50)
print("\nTest 2 : Liste avec une string")
validate([1, 2, "oops", 4])

print("\n" + "-" * 50)
print("\nTest 3 : Pas une liste")
validate("hello")

print("\n" + "-" * 50)
print("\nTest 4 : Liste vide")
validate([])


print("\n" + "=" * 70)
print("PARTIE 2 : CONVENTIONS DE NOMMAGE PYTHON")
print("=" * 70)

print("\n--- 2.1 : Les Trois Types de Noms ---\n")

print("""
┌────────────────┬──────────────────┬────────────────────────────┐
│   Convention   │     Syntaxe      │         Signification      │
├────────────────┼──────────────────┼────────────────────────────┤
│   PUBLIC       │   attr           │ Accessible partout         │
│                │   method()       │ Fait partie de l'API       │
├────────────────┼──────────────────┼────────────────────────────┤
│   PROTÉGÉ      │   _attr          │ "Usage interne suggéré"    │
│                │   _method()      │ Convention, pas forcé      │
├────────────────┼──────────────────┼────────────────────────────┤
│   PRIVÉ        │   __attr         │ Name mangling activé       │
│                │   __method()     │ Vraiment plus difficile    │
│                │                  │ d'accès de l'extérieur     │
└────────────────┴──────────────────┴────────────────────────────┘
""")


print("\n--- 2.2 : Attribut Public (normal) ---\n")

class PublicExample:
    def __init__(self):
        self.public_attr = "Je suis public"
    
    def public_method(self):
        return "Méthode publique"

obj_pub = PublicExample()

print("Accès à l'attribut public :")
print(f"  obj.public_attr = {obj_pub.public_attr}")
print("  ✓ Accès direct, aucun problème\n")

print("Accès à la méthode publique :")
print(f"  obj.public_method() = {obj_pub.public_method()}")
print("  ✓ Accès direct, aucun problème\n")

print("Modification :")
obj_pub.public_attr = "Modifié"
print(f"  obj.public_attr = {obj_pub.public_attr}")
print("  ✓ Modification autorisée\n")


print("\n--- 2.3 : Attribut Protégé (_attr) ---\n")

class ProtectedExample:
    def __init__(self):
        self._protected_attr = "Je suis protégé (par convention)"
    
    def _protected_method(self):
        return "Méthode protégée"
    
    def public_method(self):
        # Utilisation interne : OK
        return f"J'utilise {self._protected_attr}"

obj_prot = ProtectedExample()

print("IMPORTANT : '_attr' est une CONVENTION, pas une restriction !\n")

print("Accès depuis l'extérieur (techniquement possible) :")
print(f"  obj._protected_attr = {obj_prot._protected_attr}")
print("  ⚠️ Fonctionne mais c'est DÉCONSEILLÉ\n")

print("Ce que ça signifie :")
print("  → 'Je suis un détail d'implémentation'")
print("  → 'Utilisez-moi seulement dans la classe'")
print("  → 'Je peux changer sans prévenir'\n")

print("Impact sur l'import :")
print("  from module import *")
print("  → N'importe PAS les _protected")
print("  → Importe seulement les publics\n")


print("\n--- 2.4 : Attribut Privé (__attr) - NAME MANGLING ---\n")

class PrivateExample:
    def __init__(self):
        self.__private_attr = "Je suis VRAIMENT privé"
    
    def __private_method(self):
        return "Méthode privée"
    
    def public_method(self):
        # Accès interne : OK
        return f"J'utilise {self.__private_attr}"
    
    def call_private_method(self):
        # Appel interne : OK
        return self.__private_method()

obj_priv = PrivateExample()

print("NAME MANGLING : Python RENOMME l'attribut !\n")

print("Tentative d'accès normal :")
try:
    print(f"  obj.__private_attr = {obj_priv.__private_attr}")
except AttributeError as e:
    print(f"  ✗ AttributeError : {e}")
    print("  → L'attribut n'existe pas sous ce nom !\n")

print("Le vrai nom après mangling :")
print(f"  obj._PrivateExample__private_attr = "
      f"{obj_priv._PrivateExample__private_attr}")
print("  ✓ Accessible mais c'est TRÈS MAL VU\n")

print("Accès depuis la classe elle-même :")
print(f"  obj.public_method() = {obj_priv.public_method()}")
print(f"  obj.call_private_method() = {obj_priv.call_private_method()}")
print("  ✓ Fonctionne normalement à l'intérieur\n")


print("\n--- 2.5 : Visualisation du Name Mangling ---\n")

class DemoMangling:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

obj_demo = DemoMangling()

print("Attributs de l'objet (via dir()) :")
attrs = [attr for attr in dir(obj_demo) if not attr.startswith('__class')]
for attr in attrs:
    if not attr.startswith('_'):
        print(f"  ✓ {attr:30} (public)")
    elif attr.startswith('_Demo'):
        print(f"  🔒 {attr:30} (private mangé)")
    elif attr.startswith('_'):
        print(f"  ⚠️ {attr:30} (protégé)")

print("\n⚡ Observation : '__private' devient '_DemoMangling__private'\n")


print("\n--- 2.6 : Quand Utiliser Chaque Convention ? ---\n")

print("""
┌─────────────────────────────────────────────────────────────────┐
│                      QUAND UTILISER ?                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PUBLIC (attr) :                                                │
│    ✓ Fait partie de l'API publique                             │
│    ✓ Les utilisateurs DOIVENT pouvoir l'utiliser               │
│    ✓ Vous vous engagez à le maintenir stable                   │
│    Exemples : process(), validate(), data                      │
│                                                                 │
│  PROTÉGÉ (_attr) :                                              │
│    ✓ Détail d'implémentation                                   │
│    ✓ Peut être utilisé dans les sous-classes                   │
│    ✓ Peut changer dans les futures versions                    │
│    Exemples : _cache, _internal_state, _helper()               │
│                                                                 │
│  PRIVÉ (__attr) :                                               │
│    ✓ Vraiment interne à LA classe (pas les sous-classes)       │
│    ✓ Évite les conflits de noms dans l'héritage                │
│    ⚠️ RARE : utilisé surtout dans les bibliothèques            │
│    Exemples : __counter, __secret_key                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
""")


print("\n--- 2.7 : Impact RÉEL sur l'Exécution ---\n")

print("Question : Est-ce juste informatif ou ça change l'exécution ?\n")

print("RÉPONSE :\n")

print("1. PUBLIC et PROTÉGÉ (_attr) :")
print("   → Purement INFORMATIF / CONVENTION")
print("   → Aucun changement dans l'exécution")
print("   → Python ne bloque rien")
print("   → C'est pour les HUMAINS (lisibilité du code)\n")

print("2. PRIVÉ (__attr) :")
print("   → Change RÉELLEMENT le nom de l'attribut")
print("   → Impact sur l'exécution (name mangling)")
print("   → Plus difficile d'accès (mais pas impossible)")
print("   → Évite les conflits dans l'héritage\n")


print("\n--- 2.8 : Exemple de Conflit Résolu par __attr ---\n")

class Parent:
    def __init__(self):
        self.__secret = "Parent secret"
    
    def get_secret(self):
        return self.__secret

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child secret"  # NE REMPLACE PAS le parent !
    
    def get_child_secret(self):
        return self.__secret

obj = Child()

print("Sans name mangling, il y aurait conflit !")
print("Avec name mangling :\n")

print(f"Parent secret : {obj.get_secret()}")
print(f"Child secret  : {obj.get_child_secret()}")

print("\nNoms réels après mangling :")
print(f"  Parent : _Parent__secret = {obj._Parent__secret}")
print(f"  Child  : _Child__secret  = {obj._Child__secret}")

print("\n→ Pas de conflit grâce au name mangling !")


print("\n" + "=" * 70)
print("RÉCAPITULATIF FINAL")
print("=" * 70)

print("""
╔═════════════════════════════════════════════════════════════════╗
║                          all()                                  ║
╚═════════════════════════════════════════════════════════════════╝

SYNTAXE : all(iterable) → bool

COMPORTEMENT :
  • Retourne True si TOUS les éléments sont True
  • Retourne False dès qu'un False est trouvé (court-circuit)
  • all([]) → True (vérité vacue)

USAGE TYPIQUE :
  all(isinstance(x, int) for x in data)
  → Vérifie que TOUS les éléments sont des int

ÉQUIVALENT :
  for x in iterable:
      if not x:
          return False
  return True

╔═════════════════════════════════════════════════════════════════╗
║                  CONVENTIONS DE NOMMAGE                         ║
╚═════════════════════════════════════════════════════════════════╝

PUBLIC (attr) :
  • Accessible partout
  • Fait partie de l'API
  • Impact : AUCUN (normal)

PROTÉGÉ (_attr) :
  • Convention "usage interne"
  • Techniquement accessible
  • Impact : AUCUN (juste convention)
  • Non importé par "from module import *"

PRIVÉ (__attr) :
  • Name mangling : __attr → _ClassName__attr
  • Vraiment plus difficile d'accès
  • Impact : RÉEL (renommage)
  • Évite les conflits dans l'héritage

RÈGLE D'OR :
  → Utilisez PUBLIC par défaut
  → Utilisez _PROTÉGÉ pour les détails internes
  → Utilisez __PRIVÉ rarement (conflits d'héritage)
""")

print("\n" + "=" * 70)
print("FIN DE L'EXPLORATION")
print("=" * 70)