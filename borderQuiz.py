

import csv
filename = open('cb.csv', 'r')
reader = csv.DictReader(filename) #creats a dictionary of the csv file and each of its columns and rows

def initBorders(reader): # simplify where country name pairs with the list of the country border name (no country codes)
    borders = {}
    for row in reader:
        if row['country_name'] in borders: #checks if the list already exists
            borders[row['country_name']].append(row['country_border_name'].lower()) #if so append to the list with the new country,
            #.lower() so that when entering an answer case does not matter since its always normamlised to lowercase
        else:
            borders[row['country_name']] = [row['country_border_name'].lower()]#else create the start of the list with the bordering country for the new country 
    return borders
    
# initBorders may not be needed but I did it to make it easier for me to understand what I am doing

def randomCountry(reader,borders):
    import random
    p = ""
    names = [row["country_name"] for row in reader] #create an array of all countries
    con = True #initalise con (continue)
    while con: #while True
        print() 
        country = names[random.randint(0,len(names)-1)]#choose a random country (-1 might not be needed i cant remember if i need it)
        print(country) # print country
        con = guessBorders(borders, country) #reassign con based on if it should exit to menu or continue in the loop


def guessBorders(borders, country):
    print("THE COUNTRY IS {}".format(country))#.format put () into {} no need to + or ,
    initNum = len(countryBorders) #initial number of countries
    while len(countryBorders) != 0:
        guess = input("Enter a neighbouring country(0 to exit and 1 to give up): ").lower()#normalise guess to lowercase
        if guess == "0":
            return #exit to menu since its returned false (return == return None == return False)
        elif guess == "1":
            print("Remaning Countries were...")
            for g in countryBorders:
                print(g) #print leftover countries
            print("Unlucky, you guessed {} out of {}! Better luck next time!".format(initNum - len(countryBorders),initNum))# inital number of countries minus current amount 
            return True # returns True to keep you in the loop while also exiting the function
        elif guess in countryBorders:
            print("CORRECT")
            countryBorders.remove(guess)#remove country from the list
        else:
            print("WRONG")
    print("All bordering countries named... Well Done")
    return True

def chooseCountry(reader,borders): #add option to loop one country or choose a country each loop
    while True:
        print()
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

                    """)# """ multi line print
        choice = int(input())
        if choice == 1:
            randomCountry(reader,borders)
        elif choice == 2:
            chooseCountry(reader,borders)
        
        
menu(reader,filename)# start game
