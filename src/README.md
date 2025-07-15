# Exercices Python - Manipulation de chaînes, logique, et structures

Ce dépôt contient plusieurs exercices Python réalisés autour de la manipulation de chaînes, de la logique de base, et de structures comme les listes et les dictionnaires. Chaque exercice est conçu pour entraîner l'utilisation de fonctions intégrées, la vérification de types, le nettoyage de données et plus encore.

---

## Sommaire

- [1. Vérifier un palindrome](#1-vérifier-un-palindrome)
- [2. Vérifier une anagramme](#2-vérifier-une-anagramme)
- [3. Nettoyer une liste mixte](#3-nettoyer-une-liste-mixte)
- [4. Compter la fréquence des lettres](#4-compter-la-fréquence-des-lettres)

---

## 1. Vérifier un palindrome

**Nom de la fonction :** `verifie_palindrome(objet)`

### Objectif :
Vérifie si une chaîne est un **palindrome**, c’est-à-dire si elle se lit de la même manière de gauche à droite et de droite à gauche.

### Contraintes :
- Ignore les **espaces**, la **casse**, les **accents** et la **ponctuation**
- Vérifie que l’entrée est bien une `str`
- Retourne un message explicite :
  - `"C'est un palindrome"`
  - `"Ce n'est pas un palindrome"`
  - `"Entrée invalide"`

### Exemple :

```python
verifie_palindrome("Élu par cette crapule")  # → "C'est un palindrome"
verifie_palindrome(12321)                    # → "Entrée invalide"
