# Projet de Bit Packing

Projet de Bit Packing du M1-Informatique de l'UIniversité Côte d'Azur de Valentin VINCENT.

## Prérequis

- Python 3.13
- Conda (recommandé)

Le projet a été réalisé et testé dans un envireoonement de développment : anaconda (ou conda)

## Installation (si les tests sont faits avec anaconda)

1.  **Clonez le dépôt ou téléchargez les fichiers du projet.**


2. **Créez un nouvel environnement Conda au nom de votre choix:**
    ```bash
    conda create --name nom_de_lenv python=3.13
    ```

3.  **Activez l'environnement Conda :**
    ```bash
    conda activate nom_de_lenv
    ```

## Utilisation

### Pour tester le fonctionnement

Les tests pour ce projet sont inclus dans le fichier `main.py`

Il suffit de lancer le main : 
```bash
python main.py
```

Pour tester sur d'autres listes inexistante, il suffit d'en créer en suivant la manière de créer une liste de nombre comme suit : 
```python
liste = [Number(valeur), Number(valeur_2), Number(etc...), ...]
```
Et en la mettant en paramètre de la fonction `test()` qui est la seule fonction lancée dans le fichier.

Pour voir les résultats du benchmark, il faut exécuter le fichier `benchmark.py`.

### Pour lancer un benchmark

Le benchmark de projet se trouve dans le fichier `benchmark.py`

Pour le lancer il suffit de commenter les lignes n° `23`et `77` du fichier `bit_pack.py` car sinon, les résultats avec la première taille max de nombre binaire seront masqués.

```python
23    print(f"Le nombre {number.value} - {bin_number} dépasse la taille maximum d'un entier ({self.max_length}), il sera donc ignoré") # À commenter

...

77    print(f"Le nombre {number.value} (taille: {bin_size}) dépasse la taille maximum d'une piste ({self.max_length}), il sera donc ignoré") # À commenter
```

## Fichiers du Projet

-   `number.py`: Contient la classe `Number` et des fonctions utilitaires pour la conversion entre les nombres décimaux et binaires.
-   `bit_pack.py`: Contient les implémentations des algorithmes `BitPacking_v1` et `BitPacking_v2`.
-   `main.py`: Contient la fonction principale pour tester les différents alogrithmes.
-   `benchmark.py`: Contient le banchmark pour comparer l'efficacité des 2 méthodes.

