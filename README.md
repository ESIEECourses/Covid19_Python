# DashBoard Covid19
Bienvenue sur le ReadMe de notre dashboard pour le Covid19.  
L'objectif de cette application étant d'éclairer sur la situation pandémique du Covid19 en France, pour le second semestre 2021.  
Pour mieux vous accompagnez sur l'utilisation de notre application, vous trouverez ci-dessous :
  - User Guide
  - Developper Guide
  - Rapport d'analyse 


<br><br>

            
## User Guide
Pour commencer l'utilisation de notre application et visualiser les divers informations sur le Covid19, vous devez suivres les étapes suivantes pour l'implémenter sur votre machine :  
- Clonage du projet : commencer par cloner le projet sur la machine souhaité, à l'aide du lien présent dans le Git du projet.
  - Si vous clonez depuis un IDE ou un édtiteur de texte, copiez-collez ce lien :    
  ```bash
  https://github.com/ESIEECourses/Covid19_Python.git
  ```
  - Si vous clonez depuis un terminal, vous devez utilisez 'git clone' devant le lien :    
  ```bash
  git clone https://github.com/ESIEECourses/Covid19_Python.git
  ```
- Installation des packages : pour éviter d'avoir des erreurs lors du lancement de l'application, il est préférable d'installer les packages utilisés.
  ```bash
  pip install -r requirements.txt
  ```
- Lancement de l'application : pour pouvoir lancer l'application, assurez vous d'être dans le répertoire de l'application depuis le terminal et effectuer la commande suivante pour les machines windows ou linux :
  ```bash
  python main.py
  ```
  Pour les utilisateurs macOS, pas d'inquiétude ! Effectuer la commande suivante :
  ```bash
  python3 main.py
  ```

- Visualisation du dashboard : pour commencer à naviguer sur le dashboard, il vous suffirat simplement de cliquer sur l'adresse indiqué sur votre terminal ou entrer celui-ci dans un navigateur web :
  ```bash
  http://localhost:8050
  ```   


<br><br>


## Developper Guide
Ce guide est destiné aux développeurs qui souhaitent comprendre l'architecture du code, apporter des modifications ou étendre les fonctionnalités existantes.
### Structure du Projet :

- `main.py`: Contient la classe principale `Main` qui lance l'application Dash.
- `dashboard.py`: Définit la classe `DashBoard` qui crée la mise en page de l'application.
- `histogram.py`: Contient la classe `Histogram` pour la création des graphiques à barres.
- `map.py`: Définit la classe `Map` pour la création de la carte interactive.
- `data/`: Dossier contenant les fichiers de données CSV.

### Modifications et extensions possibles
- **Changer la source de données :**
  Vous pouvez modifier la source de données en remplaçant le chemin du fichier CSV dans les classes `Histogram` et `Map`.
  
- **Ajouter de nouvelles fonctionnalités :**
  Pour ajouter de nouvelles fonctionnalités, explorez les méthodes existantes dans les classes `DashBoard`, `Histogram` et `Map`. Ajoutez de nouveaux composants Dash ou des fonctionnalités de traitement de données.

- **Personnaliser l'apparence :**
  Personnalisez l'apparence en modifiant le fichier CSS dans le dossier `assets`.

- **Modifier la carte :**
  Pour apporter des modifications à la carte, explorez la classe `Map`

- **Ajouter une nouvelle visualisation :**
  Vous avez la possibilité d'ajouter de nouvelles visualisations pour enrichir votre tableau de bord. Pour cela, explorez la classe `Dashboard` et ajoutez une nouvelle méthode `create_additional_visualization()`. Vous pouvez y intégrer un nouveau type de       graphique en utilisant les données COVID-19 existantes.

- **Paramétrage dynamique de la carte :**
  Permettez aux utilisateurs de choisir les données à afficher sur la carte. Dans la classe `Map`, modifiez la méthode `add_markers()` pour accepter un paramètre `data_column`. Dans la classe `Dashboard`, ajoutez une interface utilisateur (par exemple, une     liste déroulante) pour sélectionner dynamiquement les données à afficher sur la carte.
  


<br><br>


## Rapport d'analyse
### Contexte
Notre projet consiste à éclaircir le sujet du Covid-19 en France, pour le second semestre 2021 grâce aux données provenant du site sante.gouv.fr.   
Plusieurs sujets sont abordés sur le sujet du Covid-19, mais dans notre cas on a voulu analyser le total de décès en fonction dans les divers régions, le taux de vaccination pour la dose n°1 et n°2 en fonction des âges.

### Analyse des résultats
Tout d'abord, en observant le total de dèces en France grâce à la carte, nous avons observé que :
- le taux de dèces est toujours présent dans presque toutes les régions
- l'Ile-de-France, le Nord, la Moselle, le Haut-Rhin et la Bouches-du-Rhône sont les régions avec le plus de dèces en France

Ensuite, le premier histogram à gauche sur le pourcentage des doses n°1 nous permet de conclure que :
- les enfants qui viennent de naîtres jusqu'aux 9 ans, sont très quasiment pas vaccinés
- majoritairement ce sont les personnes ayant entre 50 et 69 qui ont effectué la première dose avec environ 32%
- si on ne prend pas en compte les 0 à 9 ans, ce sont les 10 à 19 qui sont les moins vaccinés avec 5%

Enfin, le dernier histogram à droite sur le pourcentage des doses n°2 nous permet d'affirmer que :
- les enfants venaientt de naîtres et jusqu'à leurs 9 ans, n'ont pas effectué la deuxième dose
- les personnes ayant entre 50 et 59 ans, représente le plus grand pourcentage de dose n°2 avec environ 16%
- les personnes ayant entre 10 et 19 ans, représente le plus petit pourcentage de dose n°2 avec environ 5%

### Conclusion
Après deux ans de l'apparition du premier cas de Covid-19 en France, on constate que le taux de dèces en France était toujours présent avec notamment des régions plus touchées que d'autres.   
Le déploiement des premiers vaccins a permis de réduire cette hausse des dèces, où les adultes représentent la grande partie des vaccinations.   
La dose de rappel a été également en tendance, chez les adultes compris entre 50 et 59 ans.


<br><br>


## Auteurs
- Kayanthan NADARASA
- Rachid ABDOULALIME 
