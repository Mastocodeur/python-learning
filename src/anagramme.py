from typing import Union
import unidecode

def est_anagramme(mot1: Union[str, int, float], mot2: Union[str, int, float])-> str:
    """
    Vérifie si deux mots sont anagrammes
    
    Deux mots sont des anagrammes s’ils contiennent exactement les mêmes lettres, en quantité égale, mais pas nécessairement dans le même ordre.
    Ignore la casse, les espaces, les accents et la ponctuation.

    Args:
        mot1 (Union[str, int, float]): Premier mot ou phrase à comparer
        mot2 (Union[str, int, float]): Deuxième mot ou phrase à comparer

    Returns:
        str: "Entrée invalide" si l'entrée n'est pas une chaîne,
                               sinon True si anagrammes, False sinon
    """
    
    if not isinstance(mot1, str) or not isinstance(mot2, str):
        return "Entrée invalide"

    def nettoyer(texte: str) -> str:
        texte = unidecode.unidecode(texte.lower())
        return ''.join(c for c in texte if c.isalnum())

    mot1_nettoye = nettoyer(mot1)
    mot2_nettoye = nettoyer(mot2)

    return sorted(mot1_nettoye) == sorted(mot2_nettoye)
    
    
# Tests 
assert est_anagramme("nam", "man") == True
assert est_anagramme("Clint Eastwood", "Old West Action") == True
assert est_anagramme("chien", "niche") == True
assert est_anagramme("python", "java") == False
assert est_anagramme(123, "abc") == "Entrée invalide"
print("✅ Tous les tests sont passés !")