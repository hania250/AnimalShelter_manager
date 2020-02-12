
class Animal:
    def __init__(self, name, date, condition, vaccination):
        self.name = name
        self.date = date
        self.condition = condition
        self.vaccination = vaccination

    def print(self):
        print(self.name, self.date, self.condition)

    def set_vaccination(self, value):
        if self.vaccination == 'Tak':
            self.vaccination = True
        else:
            self.vaccination = False

list = []


def add_animal(name, date, condition, vaccination):
    animal = Animal(name, date, condition, vaccination)
    list.append(animal)


def print_animal(index, animal):
    print('{:2} | {:5} | {:5} | {:5} | {:5}'.format(index, animal.name, animal.date, animal.condition, animal.vaccination))
    print(animal.name, ':', animal.date, ':', animal.condition, ":", animal.vaccination)


def add_animal_from_input():
    name = input('Podaj imie: ')
    date = input('Data przyjecia: ')
    condition = input('Podaj stan: ')
    vaccination = input("czy zwierzak był szczepiony? ")
    if vaccination == "tak":
        vaccination = True
    else:
        vaccination = False
    add_animal(name, date, condition, vaccination)

#add_animal_from_input()

add_animal("z", "z", "zz", True)

for index in range(len(list)):
    print_animal(index, list[index])

index = int(input('Podaj nr indeksu: '))
animal = list[index]
animal.set_vaccination(input('Zmiana stanu szczepienia: '))
print(animal.vaccination)

for index in range(len(list)):
    print_animal(index, list[index])

# dodanie komentarza