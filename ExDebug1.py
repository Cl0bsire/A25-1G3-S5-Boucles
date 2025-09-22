def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


# Récupérer inputs
if __name__ == "__main__":
    #TODO: Créer 3 listes
    liste_temp = []
    liste_poussiere = []
    liste_humidite = []

    #TODO: Pour 3 ordinateurs
        #TODO: Demander temp, poussiere, humidite
        #TODO: Mettre les 3 valeurs dans leurs liste
for i in range(3):
    print("="*30)
    print(f"Ordinateur {i+1}")

    while True:
        try:
            temp = float(input("Entrez la température: "))
            liste_temp.append(temp)
            break
        except:
            print("Température invalide!")

    poussiere = input("Entrez le niveau de poussière (faible, moyen, élevé): ")
    liste_poussiere.append(poussiere)

    while True:
        try:
            humidite = float(input("Entrez l'humidité: "))
            liste_humidite.append(humidite)
            break
        except:
            print("Humidité invalide!")
    #TODO: Pour les 3 ordinateurs
        #TODO: utiliser la fonction et afficher le résultat


print("="*30)
print("Ordinateur 1 :")
print(environnement_optimal(liste_temp[0], liste_poussiere[0], liste_humidite[0]))
"""print(f"Ordinateur 2 : {environnement_optimal(liste_temp[1], liste_poussiere[1], liste_humidite[1])}")
print(f"Ordinateur 3 : {environnement_optimal(liste_temp[2], liste_poussiere[2], liste_humidite[2])}")"""

