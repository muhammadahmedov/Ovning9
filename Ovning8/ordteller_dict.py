# def containsNumber(value):
#     for character in value:
#         if character.isdigit():
#             return True
#     return False


ordliste = dict()
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for index, linje in enumerate(fila, start=1):
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if containsNumber(ordet) == False:
                if ordet not in ordliste:
                    ordliste[ordet] = index
    for ordet in ordliste:
        print(f"Ordet {ordet} framkommer först i linje {ordliste[ordet]}")
