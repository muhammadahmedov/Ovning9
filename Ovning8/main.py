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
        
def check(answer, shuffled_list):
    answer = int(answer)
    cities = [shuffled_list[0], shuffled_list[1], shuffled_list[2]]
    for index, city in enumerate(cities):
        if city == correctcity:
            correctcity_index = index + 1
            if answer == correctcity_index:
                print("Rätt!\n")
            else:
                print("Fel!\n")

for index, i in enumerate(countries):
    print("-------------------------------------------------------\nVad är", countries[index] + "s", "huvudstad?")
    capitals_ = capitals[:]
    capitals_.pop(index)

    random1 = random.choice(capitals_)
    capitals_.remove(random1)
    random2 = random.choice(capitals_)
    
    correctcity = capitals[index]
    shuffled_list = [random1, random2, correctcity]
    random.shuffle(shuffled_list)
    first = f"1. {shuffled_list[0]}"
    second = f"\n2. {shuffled_list[1]}"
    third = f"\n3. {shuffled_list[2]}"
    # print(f"1. {shuffled_list[0]}\n2. {shuffled_list[1]}\n3. {shuffled_list[2]}")
    print(first, second, third)
    answer = input("Svar: ")
    if answer == "":
        break
    check(answer, shuffled_list)







