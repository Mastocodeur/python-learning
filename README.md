# Fonctions Python essentielles à connaître

Ce dépôt présente les fonctions les plus courantes et utiles en Python, avec des exemples simples pour chaque cas. Il couvre les fonctions intégrées (`built-in`), ainsi que certaines fonctions fonctionnelles classiques (`map`, `filter`, `reduce`) et des modules standards comme `functools` et `itertools`.

## Table des matières

- [Introduction](#introduction)
- [Fonctions de boucle et d'itération](#fonctions-de-boucle-et-diteration)
- [Manipulation de collections](#manipulation-de-collections)
- [Chaînes de caractères](#chaînes-de-caractères)
- [Utilitaires généraux](#utilitaires-généraux)
- [Programmation fonctionnelle](#programmation-fonctionnelle)
- [Fonctions avancées](#fonctions-avancées)
- [Modules utiles](#modules-utiles)
- [Licence](#licence)

## Introduction

Python dispose d'un ensemble de fonctions intégrées très puissantes, qui permettent de coder de manière concise, lisible et efficace. Ce document regroupe les fonctions que tout développeur Python devrait connaître, avec des exemples concrets.

---

## Fonctions de boucle et d'itération

### range()

```python
for i in range(3):
    print(i)  # 0, 1, 2
```



### enumerate()

```python
noms = ["Alice", "Bob"]
for i, nom in enumerate(noms):
    print(i, nom)  # 0 Alice, 1 Bob
```

### zip()
```python
a = [1, 2]
b = ['un', 'deux']
print(list(zip(a, b)))  # [(1, 'un'), (2, 'deux')]
```
### map()

```python
nombres = [1, 2, 3]
carrés = list(map(lambda x: x**2, nombres))  # [1, 4, 9]
```

### filter()
```python
pairs = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # [2, 4]
```

### sorted()
```python
sorted([3, 1, 2])  # [1, 2, 3]
```

### reversed()
```python
list(reversed([1, 2, 3]))  # [3, 2, 1]
```

### any() / all()
```python
any([False, True, False])  # True
all([True, True, True])    # True
```

## Manipulation de collections

### len(), sum(), max(), min()
```python
len([1, 2, 3])       # 3
sum([1, 2, 3])       # 6
max([1, 5, 3])       # 5
min([1, 5, 3])       # 1
```

### type() et isinstance()


```python
type("abc")           # <class 'str'>
isinstance("abc", str)  # True
```


## Chaînes de caractères

### str(), upper(), lower(), replace(), split(), join()
```python
"abc".upper()        # "ABC"
"ABC".lower()        # "abc"
"salut toi".split()  # ["salut", "toi"]
" ".join(["salut", "toi"])  # "salut toi"
"test".replace("t", "T")    # "TesT"
```

### format() et f-strings
```python
nom = "Alice"
f"Bonjour {nom}"         # "Bonjour Alice"
"Bonjour {}".format(nom) # "Bonjour Alice"
```

## Utilitaires généraux

### print(), input(), open()
```python
print("Hello")
nom = input("Entrez votre nom: ")
with open("fichier.txt", "r") as f:
    contenu = f.read()
```


### dir(), help(), id()

```python
dir(str)       # Liste des attributs/méthodes d'une string
help(str)      # Documentation de str
id("abc")      # Identifiant mémoire
```

## Programmation fonctionnelle

### reduce() (via functools)
```python
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 10
```

### lambda
```python
f = lambda x: x * 2
f(3)  # 6
```

## Fonctions avancées

### *args et **kwargs
```python
def f(*args, **kwargs):
    print(args)
    print(kwargs)

f(1, 2, a=3, b=4)  # args: (1,2), kwargs: {'a': 3, 'b': 4}
```


### decorators
```python
def decorateur(fonction):
    def wrapper():
        print("Avant")
        fonction()
        print("Après")
    return wrapper

@decorateur
def dire_bonjour():
    print("Bonjour")

dire_bonjour()
```

## Modules utiles

### functools
`reduce()`, `lru_cache()`, `partial()`

### itertools
`chain()`, `cycle()`, `combinations()`, `product()`

### collections
`Counter`, `defaultdict`, `deque`, `namedtuple`

## Licence
Ce dépôt est disponible sous licence MIT. Vous pouvez l'utiliser, le modifier et le redistribuer librement.


