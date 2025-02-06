

import csv
filename = open('cb.csv', 'r')
reader = csv.DictReader(filename)
def initBorders(reader):
    borders = {}
    for row in reader:
        if row['country_name'] in borders:
            borders[row['country_name']].append(row['country_border_name'])
        else:
            borders[row['country_name']] = [row['country_border_name']]
    return borders
    


def randomCountry(reader,borders):
    import random
    p = ""
    codes = [row["country_code"] + "|" + row["country_name"] for row in reader]
    while True:
        p = input("Enter 0 to exit Random Selection: ")
        if p != "0":
            country = codes[random.randint(0,len(codes)-1)]
            guessBorders(borders, country[country.index("|")+1:])
        else:
            break

def guessBorders(borders, country):
    countryBorders = [ c.lower() for c in borders[country]]
    print("THE COUNTRY IS {}".format(country))
    while len(countryBorders) != 0:
        guess = input("Enter a neighbouring country(0 to exit and 1 to give up): ").lower()
        if guess == "0":
            return Nones
        elif guess == "1":
            print("Remaning Countries were...")
            for g in countryBorders: print(g)
        elif guess in countryBorders:
            print("CORRECT")
            countryBorders.remove(guess)
        else:
            print("WRONG")
    print("All bordering countries named... Well Done")

def chooseCountry(reader,borders): #add option to loop one country or choose a country each loop
    while True:
        country = input("Enter the country you want to access: ")
        if country != "0":
            guessBorders(borders, country)
        else:
            break


def menu(reader,filename):
    choice = -1
    borders = initBorders(reader)
    while choice != 0:
        print("""
            ######################################

                    WELCOME TO THE BORDER
                            QUIZ
                            
            ######################################

                    0 - Exit
                    1 - Random country selection
                    2 - Choose the country (WIP)

                    """)
        choice = int(input())
        if choice == 1:
            filename.seek(0)
            randomCountry(reader,borders)
        elif choice == 2:
            filename.seek(0)
            chooseCountry(reader,borders)
        
        
menu(reader,filename)
