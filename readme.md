# KumAutomation

Ce script Python est conçu pour interagir avec l'API Uptime Kuma. Il vous permet d'ajouter ou de supprimer des moniteurs HTTP pour des noms de domaine, soit manuellement, soit à partir d'un fichier CSV.


## Pré-requis

- Python 3.6 ou une version supérieure installée sur votre machine.
- Le package Python _uptime_kuma_api_ installé.
- F

### Installation

Les étapes pour installer votre programme....

Dites ce qu'il faut faire...

Installation du package uptime_kuma_api : Executez la commande ``pip install uptime_kuma_api`` pour commencer ensuite [...]


## Démarrage

Dites comment faire pour lancer votre projet

## Fonctionnement

Importez ``UptimeKumaApi`` et ``MonitorType`` du package ``uptime_kuma_api``.
Le script contient plusieurs fonctions :
- ``add_monitors_from_csv(api, filename):`` Cette fonction lit un fichier CSV et ajoute des moniteurs HTTP pour chaque nom de domaine listé dans le fichier.
- ``add_monitors_manually(api)`` : Cette fonction vous permet d'entrer manuellement des noms de domaine pour lesquels des moniteurs HTTP seront ajoutés.
- ``delete_all_monitors(api)``: Cette fonction supprime tous les moniteurs existants.
- ``main()``: Cette fonction exécute le script, vous invitant à choisir entre l'ajout ou la suppression de moniteurs, et entre l'entrée manuelle des noms de domaine ou leur lecture à partir d'un fichier CSV.

## Auteurs

* **Paul CAZALS** _alias_ [@pcazals](https://github.com/pcazals)



