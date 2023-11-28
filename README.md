# HydrogenLabAssistant
## How to use
Créer un fichier .txt du nom de votre choix.
La première ligne du fichier doit être le titre de votre graphe
La deuxième ligne du fichier doit être le nom de vos axes séparés par un espace.
La troisième ligne du fichier doit être la légende du graph.
Le reste comprend vos données séparées par des espaces et des retours à la ligne.
### Example
Hello World
t x
0 0
1 5
2 10
3 15

## FileManager
FileManager permet d'extraire les données du fichier .txt de votre choix.
### get_title
Permet de récuperer le titre du graphique
### get_axis
Permet de récuperer le nom des axes
### get_data(line=True)
Permet de récuperer les informations contenues dans le fichier.
Si line == True : Donne les informations ligne par ligne
Si line == False : Donne les informations par colonne

