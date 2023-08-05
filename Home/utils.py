def find_max(lists):
    maxx = lists[0]
    for i in lists:
        if i > maxx:
            maxx = i
    return maxx


def convert_weight(weight, unit):
    if weight.isdigit():  # Vérifie si la valeur est un nombre entier
        weight = int(weight)  # Convertit la valeur en entier
        if unit.lower() == 'l':
            print(f"{weight} lbs is approximately {weight / 2.20462:.2f} kg")
        elif unit.lower() == 'k':
            print(f"{weight} kg is approximately {weight * 2.20462:.2f} lbs")
        else:
            print("Wrong letter. Use 'L' for lbs or 'K' for kg.")
    else:
        print("Enter an integer for weight.")
