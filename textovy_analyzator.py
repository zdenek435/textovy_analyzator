"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Johánek

email: zdenek.johanek@infomatic.cz

discord: zdenek0004_27578

"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#print(type(TEXTS))
#text1 = TEXTS[0]        # výběr prvního textu
pocet_slov = 0
title_case_words = 0
pocet_slov_velkyma = 0
pocet_slov_malyma = 0
pocet_slov_numeric = 0
celkem_numeric = 0

delky = []
cetnost = {}
pocet = 0
"""
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123
"""
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
#print(users)
username = input("Zadej uživatelské jméno:")
password = input("Zadej heslo:")
if users.get(username) == password:
    print("_"*30, "\nWelcome to the app,", username, "\nWe have 3 texts to be analyzed.")
    print("_"*30)
    number = int(input("Enter a number btw. 1 and 3 to select:"))
    if (number >= 1) and (number <= 3):
        if number == 1: text1 = TEXTS[0]
        if number == 2: text1 = TEXTS[1]
        if number == 3: text1 = TEXTS[2]
        print("_" * 30)
        text1 = text1.replace("\n", " ")
        text1 = text1.replace(",", "")
        text1 = text1.replace(".", "")
        text1 = text1.strip()
        text1 = text1.split(" ")
        for i in text1:
            pocet_slov = pocet_slov + 1
            if i.isupper() and i.isalpha(): pocet_slov_velkyma = pocet_slov_velkyma + 1
            if i[0].isupper(): title_case_words = title_case_words + 1
            if i.islower(): pocet_slov_malyma = pocet_slov_malyma + 1
            if i.isnumeric():
                pocet_slov_numeric = pocet_slov_numeric + 1
                celkem_numeric = celkem_numeric + int(i)
        print("There are", pocet_slov, "words in the selected text.")
        print("There are", title_case_words, "titlecase words.")
        print("There are", pocet_slov_velkyma, "uppercase words.")
        print("There are", pocet_slov_malyma, "lowercase words.")
        print("There are", pocet_slov_numeric, "numeric strings.")
        print("The sum of all the numbers", celkem_numeric)
        for i in text1:
            delky.append(len(i))
        delky.sort()
        for i in delky:
            cetnost[i] = delky.count(i)
        #print(cetnost)
        pocet = 0                           #získání nejčetnějšího slova
        for i, y in cetnost.items():
            if y > pocet: pocet = y
        #print(pocet)
        print("_" * (pocet + 20))
        print("LEN |", " ", "OCCURENCES", " " * (pocet - 10), "|NR.")
        print("_" * (pocet + 20))
        for i, y in cetnost.items():
            z = len(str(i))
            if z < 2:
                print(" " * 2, f"{i}|", "*" * y, " " * (pocet - y + 2), f"|{y}")
            else:
                print(" ", f"{i}|", "*" * y, " " * (pocet - y + 2), f"|{y}")
    else:
        print("Nevybral jsi správnou hodnotu pro vyber textu, terminating the program..")
else:
    print("unregistered user, terminating the program..")