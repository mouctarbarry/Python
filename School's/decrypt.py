f4g = {}  # Dictionary to store frequencies of 4-grams
total = 0  # Total count of 4-grams

# Read data from the file and calculate frequencies
try:
    with open('brut4g_fr.txt') as f:
        for line in f:
            w, c = line.split()
            f4g[w] = int(c)
            total += int(c)

    # Calculate the frequencies
    for w in f4g:
        f4g[w] /= total

    # Print the frequency of 'MENT'
    print(f4g['MENT'])

except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Incorrect file format. Ensure each line has a 4-gram and its count separated by space.")


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}")  # Use self.name to access the instance attribute


person1 = Person("John")
person1.talk()
