
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
        vaccination = input("czy zwierzak był szczepiony? ")
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

        with open('shelter.csv', 'a+') as f:
            for line in text_animals:
                f.write(line + '\n')

bot = AnimalBot()

bot.add_animal("Abc", "10.10.2018", "ok", True)
bot.add_animal("Cde", "10.02.2018", "ok", True)
#bot.set_animal_vaccination(0,'nie')
#bot.print_vaccinated()
bot.save_animals()