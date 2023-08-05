def find_max(numbers):
    _max = numbers[0]
    for i in numbers:
        if i > _max:
            _max = i
    return _max


def convert_weight(weight, unit):
    if isinstance(weight, int):  # Vérifie si la valeur est un nombre entier
        weight = int(weight)  # Convertit la valeur en entier
        if unit.lower() == 'l':
            print(f"{weight} lbs is approximately {weight / 2.20462:.2f} kg")
        elif unit.lower() == 'k':
            print(f"{weight} kg is approximately {weight * 2.20462:.2f} lbs")
        else:
            print("Wrong letter. Use 'L' for lbs or 'K' for kg.")
    else:
        print("Enter an integer for weight.")
