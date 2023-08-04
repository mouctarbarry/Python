poids = input("Weight : ")
unit = input("(L)bs or (K)g: ")

if poids.isdigit():  # Vérifie si la valeur est un nombre entier
    poids = int(poids)  # Convertit la valeur en entier

    if unit.lower() == 'l':
        print(f"{poids} lbs is approximately {poids / 2.20462:.2f} kg")
    elif unit.lower() == 'k':
        print(f"{poids} kg is approximately {poids * 2.20462:.2f} lbs")
    else:
        print("Wrong letter. Use 'L' for lbs or 'K' for kg.")
else:
    print("Enter an integer for weight.")
