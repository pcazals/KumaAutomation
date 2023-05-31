# KumAutomation

Ce script Python est conçu pour interagir avec l'API Uptime Kuma. Il vous permet d'ajouter ou de supprimer des moniteurs HTTP ou PING pour des noms de domaine, soit manuellement, soit à partir d'un fichier CSV.

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

Dans un premier temps renseigner l'ip de votre serveur, ex : ``192.168.0.254`` (ip seulement, le script considère que le port et celui par défaut) et vos identifiants. 
On vous demandera d'entrer votre choix d'opération (ajouter ou supprimer des moniteurs) et votre choix de méthode d'entrée (manuel ou fichier CSV).

- Si vous choisissez d'ajouter des moniteurs à partir d'un fichier CSV, assurez-vous que le fichier CSV contient un nom de domaine suivi du protocole de sonde qui va être utilisé : ``google.fr,PING``. Il faudra en entête du fichier csv avoir la ligne ``fqdn,proto``. Un fichier csv se trouve sur le repo ICI : https://github.com/pcazals/ressource/sites.csv

- Si vous choisissez d'ajouter des moniteurs manuellement, on vous demandera d'entrer chaque nom de domaine individuellement suivi du type de sonde : ``google.fr`` Puis le script vous demande si c'est une sonde ``HTTP`` ou ``PING``. Une fois finis entrer : ``quitter``.

- Si vous choisissez de supprimer des moniteurs, tous les moniteurs existants seront supprimés sans autre confirmation.

- Après chaque action, le script reviens au menu d'accueil et vous pouvez naviger pour éxecuter à nouveau les différentes fonctions.
Pour quitter le script : appuyer sur la touche 3.

## Fonctionnement du code 

Importez ``UptimeKumaApi`` et ``MonitorType`` du package ``uptime_kuma_api``.
Le script contient plusieurs fonctions :
- ``ajouter_sondes_depuis_csv(api, nom_fichier):`` Cette fonction lit un fichier CSV et ajoute des moniteurs pour chaque nom de domaine listé dans le fichier, en fonction du type de sonde indiqué (HTTP ou PING).
- ``ajouter_sondes_manuellement(api)`` : Cette fonction vous permet d'entrer manuellement des noms de domaine pour lesquels des moniteurs seront ajoutés, ainsi que le type de sonde à utiliser (HTTP ou PING).
- ``supprimer_sondes(api)``: Cette fonction supprime tous les moniteurs existants.
- ``main()``: Cette fonction exécute le script, vous invitant à choisir entre l'ajout ou la suppression de moniteurs, et entre l'entrée manuelle des noms de domaine ou leur lecture à partir d'un fichier CSV. Elle vous permet également de quitter le script.

## Diagramme de fonctionnement ##

![alt text](https://github.com/pcazals/KumaAutomation/blob/main/ressource/schemascript.png)

## Auteurs

* **Paul CAZALS** _alias_ [@pcazals](https://github.com/pcazals)
