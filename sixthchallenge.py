chaine = input("Saisissez votre chaine de charactere : ")
chaine2 = ""
for lettre in reversed(chaine) :
    chaine2 += lettre
print(chaine2)