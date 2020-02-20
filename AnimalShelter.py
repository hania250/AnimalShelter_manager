
class Animal:
    def __init__(self, name, date, condition, vaccination):
        self.name = name
        self.date = date
        self.condition = condition
        self.vaccination = vaccination

    def print(self):
        print(self.name, self.date, self.condition)

    def set_vaccination(self, value):
        if value == 'tak':
            self.vaccination = True
        else:
            self.vaccination = False

class AnimalBot:
    def __init__(self):
        self.list = []

    def add_animal(self, name, date, condition, vaccination):
        a = Animal(name, date, condition, vaccination)
        self.list.append(a)

    def print_animal(self, index):
        animal = self.list[index]
        print('{:2} | {:5} | {:5} | {:5} | {:5}'.format(index, animal.name, animal.date, animal.condition, animal.vaccination))

    def add_animal_from_input(self):
        name = input('Podaj imie: ')
        date = input('Data przyjecia: ')
        condition = input('Podaj stan: ')
        vaccination = input("Czy zwierzak był szczepiony? ")
        if vaccination == "tak":
            vaccination = True
        else:
            vaccination = False
        self.add_animal(name, date, condition, vaccination)

    def print_all_animals(self):
        for index in range(len(self.list)):
            self.print_animal(index)

    def set_animal_vaccination(self, animal_index, vaccination):
        animal = self.list[animal_index]
        animal.set_vaccination(vaccination)

    def print_vaccinated(self):
        for i in range(len(self.list)):
            animal = self.list[i]
            if animal.vaccination:
                self.print_animal(i)

    def save_animals(self):
        text_animals = []
        for i in range(len(self.list)):
            animal = self.list[i]
            text = '{};{};{};{}'.format(animal.name, animal.date, animal.condition, animal.vaccination)
            text_animals.append(text)

        with open('shelter.csv', 'w') as f:
            for line in text_animals:
                f.write(line + '\n')

    def load_animals(self):
        with open('shelter.csv', 'r') as f:
            for line in f:
                animal_list = line.split(';') # tworzy listę elementow

                if animal_list[3] == 'True\n':
                    vaccination = True
                else:
                    vaccination = False
                self.add_animal(animal_list[0], animal_list[1], animal_list[2], vaccination)

bot = AnimalBot()
bot.load_animals()

while True:
    command = input('Co chcesz zrobic? ')

    if command == 'dodaj':
        bot.add_animal_from_input()
    elif command == 'wszystkie':
        bot.print_all_animals()
    elif command == 'zmien':
        index = int(input('Podaj indeks:'))
        vaccination = input('czy byl szczepiony? ')
        bot.set_animal_vaccination(index, vaccination)
    elif command == 'pokaz zaszczepione':
        bot.print_vaccinated()
    elif command == 'zapisz':
        bot.save_animals()
    else:
        print('Nie wiem co zrobic ')