import unidecode
from typing import Union


def verifie_palindrome(objet):
    if not isinstance(objet, str):
        return "Entrée invalide"
    else:
        # Normalisation : minuscules, sans accents, sans espaces
        objet = unidecode.unidecode(objet.replace(" ","").lower())
        # Garde seulement lettres et chiffres
        objet = ''.join(c for c in objet if c.isalnum())
        if objet == objet[::-1]: 
            return "C'est un palindrome"
        else : 
            return "Ce n'est pas un palindrome"


# Version Typée et avec Docstring
def verifie_palindrome(objet: Union[str, int, float]) -> str:
    """
    Vérifie si une chaîne de caractères est un palindrome.

    Un palindrome est un mot ou une phrase qui se lit de la même façon
    de gauche à droite et de droite à gauche, en ignorant les espaces,
    la casse et les accents.

    Paramètres :
    - objet (str) : La chaîne à tester.

    Retourne :
    - str : "C'est un palindrome" si c'en est un,
            "Ce n'est pas un palindrome" sinon,
            "Entrée invalide" si l'entrée n'est pas une chaîne.
    """
    if not isinstance(objet, str):
        return "Entrée invalide"

    # Normalisation : minuscules, sans accents, sans espaces
    objet = unidecode.unidecode(objet.replace(" ", "").lower())
    # Garde seulement lettres et chiffres
    objet = ''.join(c for c in objet if c.isalnum())

    if objet == objet[::-1]: 
        return "C'est un palindrome"
    else: 
        return "Ce n'est pas un palindrome"

# Tests 
assert verifie_palindrome("Kayak") == "C'est un palindrome"
assert verifie_palindrome("Élu par cette crapule") == "C'est un palindrome"
assert verifie_palindrome("Bonjour") == "Ce n'est pas un palindrome"
assert verifie_palindrome(12321) == "Entrée invalide"
print("✅ Tous les tests sont passés !")
