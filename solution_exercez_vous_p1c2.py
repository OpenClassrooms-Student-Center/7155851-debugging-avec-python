def direBonjourOuBonsoir(nombreDeFois, prenom):
    choix = input("Tapez 1 pour dire Bonjour et 2 pour dire Bonsoir")
    if choix == "1":
        i = 0
        while i < nombreDeFois:
            print(f"Bonjour {prenom}")
            i = i + 1
    elif choix == str(2):
        for i in range(0, nombreDeFois):
            print(f"Bonsoir {prenom}")
    else:
        print("Je n'ai pas compris votre choix")

direBonjourOuBonsoir(5, "Bob")
