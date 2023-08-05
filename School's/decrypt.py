f4g = {}  # dic des fréquences des 4-grammes
f = open('brut4g_fr.txt')
total = 0  # effectif total
for line in f:
    (w, c) = line.split()
    f4g[w] = int(c)
    total += int(c)
    print(total)
for w in f4g:
    f4g[w] /= total  # calcul des fréquences
    # print (f4g)
f.close()
print(f4g['MENT'])


class Person:
    def __init__(self, name):
        self.name = name

    def named(self):
        print(f"Hello {self.name}")  # Use self.name to access the instance attribute

    def talk(self):
        print(f"{self.name} speaks English")  # Use self.name to access the instance attribute


# Creating an instance of the Person class
person1 = Person("John")

# Calling the named method to greet the person
person1.named()

# Calling the talk method to describe the language the person speaks
person1.talk()
