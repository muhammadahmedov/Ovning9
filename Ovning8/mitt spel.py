import random

with open("capitalcities.txt", "r") as capitals_file, open("countries.txt", "r") as countries_file:
    capitals = list()
    countries = list()
    for city in capitals_file:
        city = city.strip()
        capitals.append(city)
        
    for country in countries_file:
        country = country.strip()
        countries.append(country)
    
class Multiple_choices:
    
    def __init__(self, answer, countries, capitals):
        self.answer = answer
        self.countries = countries
        self.capitals = capitals
     
            
if __name__ == "__main__":
    data = Multiple_choices(input("Svar: "), countries, capitals)
    for index, i in enumerate(lista):
            if i == correct:
                if answer == index + 1:
                    print("Rätt!\n")
                else:
                    print("Fel!\n")