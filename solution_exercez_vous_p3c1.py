from datetime import *

try:
    date_de_naissance = int(input("Quelle est votre date de naissance ?"))
    age = int(datetime.now().strftime("%Y")) - date_de_naissance
except:
    print("Oups, une erreur s'est glissée dans le code.")
    while True:
        try:
            date_de_naissance = int(input("Indiquer votre date de naissance, mais uniquement des chiffres."))
            if type(date_de_naissance) == int:
                age = int(datetime.now().strftime("%Y")) - int(date_de_naissance)
                print(f"Tu as donc {age} ans.")
                break
        except:
            print("Mince, une autre erreur s'est glissée dans le code.")  
else:
    print(f"Tu as donc {age} ans.")
