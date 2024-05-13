# Outil de Génération de Texte et d'Annotation d'Images

Ce projet permet l'annotation manuelle d'images de "Carte Vitale" et de "Titre de Séjour" utilisant Label Studio, un outil d'annotation open-source, suivie de la génération de texte sur les champs effacés, et de l'utilisation de techniques d'augmentation d'image pour diversifier le jeu de données.

## Fonctionnalités

- **Annotation Manuelle avec Label Studio :** Annotation manuellement les images à l'aide de Label Studio et télécharger les fichiers JSON contenant les annotations.
- **Génération de Texte :** Généreration automatiquement du texte aléatoire sur les parties effacées des images avec un contrôle total sur le style, la taille et le placement de la police.
- **Augmentation d'Image :** Appliquation différentes techniques d'augmentation d'image pour créer un jeu de données varié.
- **Application Streamlit :** Une application Streamlit conviviale pour gérer les processus ci-dessus.

## Commencer

Ces instructions vous permettront d'obtenir une copie du projet en fonctionnement sur votre machine locale à des fins de développement et de test.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- Python 3.x
- pip

### Installation

1. Clonez le dépôt sur votre machine locale :

   ```git clone [url-du-dépôt]```
   ```cd [nom-du-dossier-du-dépôt]```

2. Créez un environnement virtuel :
    ```python -m venv venv```

3. Activez l'environnement virtuel :

    Sur Windows :
    ```.\venv\Scripts\activate```

    Sur Unix ou MacOS :
    ```source venv/bin/activate```

4. Installez les packages requis :
    ```pip install -r requirements.txt```

### Lancer l'Application
``` streamlit run app.py ```


### TEST
Le fichier test.py vous aide à comprendre la fonctionalité basique


### Pour nouvelle type d'image

- Utiliser Label Studio pour annoter nouvelle image ,telecharger les annotation au format json.
- Utiliser l'outille de erison pour supprimer les champs annotés sur nouvelle image
- Creer des fonctionnalités supplimentaires en utilisant et inspirants les fonctions du fichier utils.py 

