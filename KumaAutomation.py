from uptime_kuma_api import UptimeKumaApi, MonitorType
import csv

def obtenir_infos_serveur():
    ip_serveur = input("Entrez l'IP du serveur (! IP SEULE ! ): ")
    nom_utilisateur = input("Entrez le nom d'utilisateur : ")
    mot_de_passe = input("Entrez le mot de passe : ")
    api_url = f"http://{ip_serveur}:3001"
    return api_url, nom_utilisateur, mot_de_passe

def ajouter_sondes_depuis_csv(api, nom_fichier):
    count = 0
    with open(nom_fichier, 'r') as f:
        lecteur = csv.reader(f)
        next(lecteur, None) 
        for ligne in lecteur:
            if len(ligne) > 1:
                nom_domaine, type_sonde = ligne
                type_sonde = type_sonde.lower()

                if type_sonde == 'http':
                    api.add_monitor(type=MonitorType.HTTP, name=nom_domaine, url=f"http://{nom_domaine}")
                    count += 1
                elif type_sonde == 'ping':
                    api.add_monitor(type=MonitorType.PING, name=nom_domaine, hostname=nom_domaine)
                    count += 1
    return count

def ajouter_sondes_manuellement(api):
    count = 0
    while True:
        nom_domaine = input("Entrez un nom de domaine (ou 'quitter' pour terminer) : ")
        if nom_domaine.lower() == 'quitter':
            break

        type_sonde = input("Quel type de sonde souhaitez-vous ? (HTTP ou PING) : ")
        type_sonde = type_sonde.lower()

        if type_sonde == 'http':
            api.add_monitor(type=MonitorType.HTTP, name=nom_domaine, url=f"http://{nom_domaine}")
            count += 1
        elif type_sonde == 'ping':
            api.add_monitor(type=MonitorType.PING, name=nom_domaine, hostname=nom_domaine)
            count += 1
        else:
            print("Type de sonde invalide. Veuillez entrer 'HTTP' ou 'PING'.")

    return count

def supprimer_sondes(api):
    sondes = api.get_monitors()
    count = 0
    for sonde in sondes:
        api.delete_monitor(sonde['id'])
        count += 1
    return count

def main():
    api_url, nom_utilisateur, mot_de_passe = obtenir_infos_serveur()

    with UptimeKumaApi(api_url) as api:
        api.login(nom_utilisateur, mot_de_passe)
        while True:
            print("Bienvenue dans le script de création automatique de sondes :")
            print("1 : Création automatique")
            print("2 : Supprimer les sondes")
            print("3 : Quitter le script")

            choix = input("Entrez votre choix (1, 2 ou 3) : ")
            if choix == '1':
                sous_choix = input("Souhaitez-vous (1) Entrer les noms de domaine manuellement ou (2) Utiliser un fichier CSV ? ")
                if sous_choix == '1':
                    count = ajouter_sondes_manuellement(api)
                    print(f"{count} sondes ont été ajoutées.")
                elif sous_choix == '2':
                    nom_fichier_csv = input("Entrez le chemin vers le fichier CSV : ")
                    count = ajouter_sondes_depuis_csv(api, nom_fichier_csv)
                    print(f"{count} sondes ont été ajoutés depuis le fichier CSV.")
                else:
                    print("Choix invalide. Veuillez entrer '1' ou '2'.")
            elif choix == '2':
                count = supprimer_sondes(api)
                print(f"{count} sondes ont été supprimées.")
            elif choix == '3':
                print("Quitter le script.")
                break
            else:
                print("Choix invalide. Veuillez entrer '1', '2' ou '3'.")

if __name__ == '__main__':
    main()
