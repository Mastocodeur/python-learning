import unidecode
from typing import Any, List


def nettoyer_liste(liste: List[Any]) -> List[str]:
    """Nettoyer une liste mixte

    Args:
        liste (List[Any]): liste contenant des éléments de types variés (entiers, chaînes, None, booléens, listes imbriquées, etc.)

    Returns:
        List[str]: une nouvelle liste contenant uniquement les chaînes de caractères non vides, nettoyées :
        * supprimées de leurs espaces en trop (avant/après)
        * converties en minuscules
        * sans accents
    """
    new_liste = []
    for element in liste:
        if isinstance(element, str):
            element = unidecode.unidecode(element.strip().lower())
            if element !="":
                new_liste.append(element)
    return new_liste


# Version méga optimisée : 
"""
def nettoyer_liste(liste: List[Any]) -> List[str]:
    return [
        unidecode.unidecode(e.strip().lower())
        for e in liste
        if isinstance(e, str) and e.strip() != ""
    ]
"""

assert nettoyer_liste(["  Salut ", None, 123, True, "Éléphant", "", " BONJOUR "]) == ["salut", "elephant", "bonjour"]
assert nettoyer_liste(["", "Python", ["liste"], " C O D E ", False]) == ["python", "c o d e"]
print("✅ Tous les tests sont passés !")