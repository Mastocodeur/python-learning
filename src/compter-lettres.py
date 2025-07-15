import unidecode
from functools import reduce
from typing import List, Tuple, Dict

def preparer_lettres(texte: str) -> List[Tuple[str, int]]:
    # Normalisation : minuscules, sans accents
    texte = unidecode.unidecode(texte.lower())
    
    # Filtrage des lettres uniquement
    lettres = filter(str.isalpha, texte)

    # Mapping : chaque lettre devient (lettre, 1)
    return list(map(lambda c: (c, 1), lettres))


print(preparer_lettres("Éléphant! élégant..."))
# → [('e', 1), ('l', 1), ('e', 1), ('p', 1), ('h', 1), ('a', 1), ('n', 1), ('t', 1), ('e', 1), ...]


def reduire_frequence(paires: List[Tuple[str, int]]) -> Dict[str, int]:
    """
    Agrège une liste de (lettre, 1) en un dictionnaire {lettre: fréquence}
    """
    def accumuler(dico: Dict[str, int], pair: Tuple[str, int]) -> Dict[str, int]:
        lettre, count = pair
        dico[lettre] = dico.get(lettre, 0) + count
        return dico

    return reduce(accumuler, paires, {})

def compter_lettres(texte: str) -> Dict[str, int]:
    """
    Compte les lettres du texte avec map + reduce
    """
    paires = preparer_lettres(texte)
    return reduire_frequence(paires)


texte = "Éléphant! élégant..."
paires = preparer_lettres(texte)
print(reduire_frequence(paires))
print(compter_lettres("Éléphant élégant"))
# → {'e': 4, 'l': 2, 'p': 1, 'h': 1, 'a': 2, 'n': 2, 't': 2, 'g': 1}
