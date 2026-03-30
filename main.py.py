import random 
print(50*"-","WELCOME TO THE WORLD TRADING GAME",50*"-")
print()
print("This game is of Selling and Buying of different countries.\nIt is a unique and quite popular game which give you an opportunity to act as a international banker or a foreign buisness man.")
print()
print("RULES:")
print("1.User and AI have a fixed amount of 2 Million during the whole game.\n2.The game is started by a User followed by AI.\n3.In this game you will get country and it is your choice do you want to buy or not.\n4.If you do not want to buy you can ask the Ai to buy.\n5.If AI says no then game will continue.\n6.After every turn of both(user and Ai) the game will ask Do you want to continue.\n7.If you say 'no' it will stop the game there and display the winner.\n8.Winner will be the one you has more countries and Money.\n9.Suppose the Ai has more country but less money than user ...in that case no one will be the winner and match is DRAW.\n10.ALL THE BEST FOR THE GAME...BECAME THE BEST TRADER!!")
print()
Countries=countries = {"India": 15300,"United States of America": 18750,"China": 12450,"Brazil": 9800,"Germany": 14500,"France": 13200,
    "United Kingdom": 11000,"Italy": 9700,"Russia": 8000,"Canada": 12300,"Australia": 11900,"Japan": 19500,"South Korea": 10100,"Mexico": 8700,
    "South Africa": 6500,"Argentina": 7200,"Spain": 12800,"Saudi Arabia": 15400,"Indonesia": 9400,"Netherlands": 11300,"Sweden": 9100,
    "Norway": 8600,"Switzerland": 17800,"Egypt": 4500,"Turkey": 9900,"Thailand": 7600,"Vietnam": 6400,"Nigeria": 5000,"Kenya": 4100,
    "Ethiopia": 3800,"Pakistan": 8800,"Bangladesh": 6100,"Nepal": 3000,"Sri Lanka": 5200,"Malaysia": 8700,"Philippines": 8900,"Singapore": 19800,
    "United Arab Emirates": 17600,"New Zealand": 8700,"Poland": 9400,"Portugal": 9300,"Greece": 8500,"Denmark": 12700,"Finland": 9900,
    "Ireland": 11800,"Israel": 10300,"Chile": 8800,"Colombia": 9200,"Peru": 7600,"Venezuela": 4200}
user_money=2000000
user_country=[]
Ai_money=2000000
Ai_country=[]
number_on_dice=[1,2,3,4,5,6]
Computer_choice=["yes","no"]
while True:
    asked_countries=set()

    user_dice=random.choice(number_on_dice)
    print("User dice number: ",user_dice)
    for i in range(len(Countries)):
        if user_dice==i and i not in asked_countries:
            asked_countries.add(i)
            Country=(list(Countries.keys()))[i]
            Money=(list(Countries.values()))[i]
            print("Country:",Country)
            print("Price:",Money)
            Buy=input("Do you want to buy the country(User)? (Yes / No): ").lower()
            if Buy=="yes" and user_dice==i:
                user_country.append(Country)
                user_money-=Money
            else:
                Trade=random.choice(Computer_choice).lower()
                print("Do Ai wants a country: (Yes/ No)",Trade)
                if Trade=="yes":
                    Ai_country.append(Country)
                    Ai_money-=Money
                else:
                    continue

    Ai_dice=random.choice(number_on_dice)
    print("Ai dice number: ",Ai_dice)
    for i in range(len(Countries)):
        if Ai_dice==i and i not in asked_countries:
            asked_countries.add(i)
            Country=(list(Countries.keys()))[i]
            Money=(list(Countries.values()))[i]
            print("Country:",Country)
            print("Price:",Money)
            Buy=random.choice(Computer_choice).lower()
            print("Do Ai want to buy the country(AI)? (Yes/ No)",Buy)
            if Buy=="yes" and Ai_dice==i:
                Ai_country.append(Country)
                Ai_money-=Money
            else:
                Trade=input("Do user wants a country (Yes/No):",).lower()
                if Trade=="yes":
                    user_country.append(Country)
                    user_money-=Money
                else:
                    continue
    print()
    print("User left Money",user_money)
    print("User Country:",set(user_country))
    print()
    print("Ai left Money",Ai_money)
    print("AI country:",set(Ai_country))
    print()
    continuing=input("Do you want to continue the game?(Yes/No):").lower()
    if continuing=="no":
        break
    else:
        continue

User_Country=len(user_country)
ai_Country=len(Ai_country)
if (User_Country>ai_Country) and (user_money>Ai_money):
    print("YAY! YOU WIN THE BANK TRADING GAME")
    print("User left Money",user_money)
    print("User Country:",user_country)
elif (User_Country<ai_Country) and (user_money<Ai_money):
    print("YAY! AI WIN THE BANK TRADING GAME")
    print("Ai left Money",Ai_money)
    print("AI country:",Ai_country)
else:
    print("DRAW! NO ONE IS WINNER")




    

                

            



                   