ordliste = dict()
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for index, linje in enumerate(fila, start=1):
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if ordet not in ordliste:
                ordliste[ordet] = index
    for ordet in ordliste:
        print(f"Ordet {ordet} framkommer först i linje {ordliste[ordet]}")
        
##############################################################################

import random

with open("capitalcities.txt", "r", encoding="UTF8") as capitals_file, open("countries.txt", "r", encoding="UTF8") as countries_file:
    capitals = list()
    countries = list()
    for city in capitals_file:
        city = city.strip()
        capitals.append(city)
        
    for country in countries_file:
        country = country.strip()
        countries.append(country)

class Quiz:
    def __init__(self, capitals, for_user, correctcity, index):
        self.capitals = capitals
        self.for_user = for_user
        self.correctcity = correctcity
        self.index = index
    
    def randoms(self):
        capitals_ = self.capitals[:]
        capitals_.remove(self.correctcity)

        random1 = random.choice(capitals_)
        capitals_.remove(random1)
        random2 = random.choice(capitals_)
        shuffled_list = [random1, random2, self.correctcity]
        random.shuffle(shuffled_list)
        return shuffled_list
    
    def options(self, shuffled_list):
        self.for_user.append(f"1. {shuffled_list[0]}")
        self.for_user.append(f"\n2. {shuffled_list[1]}")
        self.for_user.append(f"\n3. {shuffled_list[2]}")
    
    def check(self, shuffled_list, answer):
        cities = [shuffled_list[0], shuffled_list[1], shuffled_list[2]]
        for index, city in enumerate(cities):
            if city == self.correctcity:
                correctcity_index = index + 1
                if answer == correctcity_index:
                    print("Rätt!\n")
                else:
                    print("Fel! Huvudstaden är", self.correctcity + ".\n")
        
    def __str__(self):
        return f"{self.for_user[0]}{self.for_user[1]}{self.for_user[2]}"

for index, country in enumerate(countries):
    correctcity = capitals[index]
    print("-------------------------------------------------------\nVad är", country + "s", "huvudstad?")
    start = Quiz(capitals, list(), correctcity, index)
    shuffled_list = start.randoms()
    start.options(shuffled_list)
    print(start)
    try:
        answer = int(input("Svar: "))
        while answer > 3 or answer <= 0:
            answer = int(input("Finns inte med i listan, försök igen: "))
        start.check(shuffled_list, answer)
    except ValueError:
        print("Quizet avbryts...")
        break
    