try :
    prenom = input("saisissez votre prenom: ")


    salaire_horaire = float(input("saisissez le salaire horaire: "))
    heures = float(input("Combien d'heure de travail ?: "))
    salaire = 0
    salaire_heure_sup = salaire_horaire * 1.5
    heure_sup = heures - 40

    if heures > 40 :
        salaire = (heure_sup * salaire_heure_sup)+(40 * salaire_horaire)
        print(f"Monsieur {prenom} a travaille {heures} heures et a obtenu {salaire} dirhams")
    else :
        salaire = heures * salaire_horaire
        print(f"Monsieur {prenom} a travaille {heures} heures et a obtenu {salaire} dirhams")
except ValueError: 
    print("Saisie incorrecte")
    exit(0) 
