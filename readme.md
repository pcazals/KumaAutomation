# KumAutomation

Ce script Python est conçu pour interagir avec l'API Uptime Kuma. Il vous permet d'ajouter ou de supprimer des moniteurs HTTP pour des noms de domaine, soit manuellement, soit à partir d'un fichier CSV.

## Pré-requis

- Python 3.6 ou une version supérieure installée sur votre machine.
- Le package Python _uptime_kuma_api_ installé.
- Une instance d'Uptime Kuma online 

### Installation

- Installation du package uptime_kuma_api : Executez la commande ``pip install uptime_kuma_api`` [...]

Si vous n'avez pas d'instance Uptime Kuma : 
- Executez la commande ``docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1``


## Utilisation

Pour exécuter le script, il suffit de l'exécuter dans votre environnement Python. 
- Executez la commande ``python3 KumaAutomation.py``

On vous demandera d'entrer votre choix d'opération (ajouter ou supprimer des moniteurs) et votre choix de méthode d'entrée (manuel ou fichier CSV).

- Si vous choisissez d'ajouter des moniteurs à partir d'un fichier CSV, assurez-vous que le fichier CSV contient un nom de domaine par ligne, sans ligne d'en-tête.
- Si vous choisissez d'ajouter des moniteurs manuellement, on vous demandera d'entrer chaque nom de domaine individuellement. Entrez ``quit`` lorsque vous avez terminé.
- Si vous choisissez de supprimer des moniteurs, tous les moniteurs existants seront supprimés sans autre confirmation.
Note


## Fonctionnement du code 

Importez ``UptimeKumaApi`` et ``MonitorType`` du package ``uptime_kuma_api``.
Le script contient plusieurs fonctions :
- ``add_monitors_from_csv(api, filename):`` Cette fonction lit un fichier CSV et ajoute des moniteurs HTTP pour chaque nom de domaine listé dans le fichier.
- ``add_monitors_manually(api)`` : Cette fonction vous permet d'entrer manuellement des noms de domaine pour lesquels des moniteurs HTTP seront ajoutés.
- ``delete_all_monitors(api)``: Cette fonction supprime tous les moniteurs existants.
- ``main()``: Cette fonction exécute le script, vous invitant à choisir entre l'ajout ou la suppression de moniteurs, et entre l'entrée manuelle des noms de domaine ou leur lecture à partir d'un fichier CSV.

## UML Diagram ##

![alt text](https://github.com/pcazals/[reponame]/blob/[branch]/image.jpg?raw=true)

## Auteurs

* **Paul CAZALS** _alias_ [@pcazals](https://github.com/pcazals)



