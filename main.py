# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from Appetizer import Appetizer, ChooseAppetizer
from Drinks import Drinks, ChooseDrinks
from Oriental import BreakfastEastren_Food, ChooseEastren_Food, LunchEastren_Food, DinnerEastren_Food
from Sweets import Sweets, ChooseSweets

def deleteAllFile():
    if os.path.exists("Data Files/FoodOutput.txt"):
        os.remove("Data Files/FoodOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/ResOutput.txt"):
        os.remove("Data Files/ResOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/TimeOutput.txt"):
        os.remove("Data Files/TimeOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/sweetsOutput.txt"):
        os.remove("Data Files/sweetsOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/drinkOutput.txt"):
        os.remove("Data Files/drinkOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/orientalOutput.txt"):
        os.remove("Data Files/orientalOutput.txt")
        # print("done")
    else:
        print("The file does not exist")

    if os.path.exists("Data Files/appetizerOutput.txt"):
        os.remove("Data Files/appetizerOutput.txt")
        # print("done")
    else:
        print("The file does not exist")
    pass

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def getDrinks(elementDrinks):
    element = elementDrinks
    ke = ChooseDrinks()
    ke.reset()
    ke.declare(
        Drinks(cacao=element["cacao"]),
        Drinks(coffee=element["coffee"]),
        Drinks(milk=element["milk"]),
        Drinks(nescafe=element["nescafe"]),
        Drinks(lemon=element["lemon"]),
        Drinks(mint=element["mint"]),
        Drinks(apple=element["apple"]),
        Drinks(banana=element["banana"]),
        Drinks(orange=element["orange"]),
        Drinks(honey=element["honey"]),
        Drinks(strawberry=element["strawberry"]),
        Drinks(mango=element["mango"]),
        Drinks(avocado=element["avocado"]),
        Drinks(melon=element["melon"]),
        Drinks(carrots=element["carrots"]),
        Drinks(cranberry=element["cranberry"]),
        Drinks(watermelon=element["watermelon"]),
        Drinks(kiwi=element["kiwi"]),
        Drinks(pineapple=element["pineapple"]),
        Drinks(oats=element["oats"]),
        Drinks(cream=element["cream"]),
        Drinks(tea=element["tea"]),
    )
    ke.run()
    pass

def getAppetizer(elementAppetizer):
    element = elementAppetizer
    ke = ChooseAppetizer()
    ke.reset()
    ke.declare(
        Appetizer(watercrees=element["watercrees"]),
        Appetizer(sumac=element["sumac"]),
        Appetizer(gourd=element["gourd"]),
        Appetizer(eggs=element["eggs"]),
        Appetizer(tomato=element["tomato"]),
        Appetizer(shrimp=element["shrimp"]),
        Appetizer(cuokumbber=element["cuokumbber"]),
        Appetizer(spinach=element["spinach"]),
        Appetizer(watermelon=element["watermelon"]),
        Appetizer(cheese=element["cheese"]),
        Appetizer(potato=element["potato"]),
        Appetizer(parsley=element["parsley"]),
        Appetizer(yogurt=element["yogurt"]),
        Appetizer(corn=element["corn"]),
        Appetizer(venus=element["venus"]),
        Appetizer(mashroom=element["mashroom"]),
        Appetizer(chicken=element["chicken"]),
        Appetizer(ozyychip=element["ozyychip"]),
        Appetizer(eggplant=element["eggplant"]),
        Appetizer(tahina=element["tahina"]),
        Appetizer(cauliflower=element["cauliflower"]),
        Appetizer(garlic=element["garlic"]),
        Appetizer(chickpeas=element["chickpeas"]),
        Appetizer(meat=element["meat"]),
        Appetizer(lemon=element["lemon"]),
        Appetizer(flour=element["flour"]),
        Appetizer(beard=element["beard"]),
        Appetizer(beans=element["beans"]),
        Appetizer(redpepper=element["redpepper"]),
        Appetizer(beet=element["beet"]),
        Appetizer(walnut=element["walnut"]),
        Appetizer(magi=element["magi"]),
        Appetizer(lentil=element["lentil"]),
        Appetizer(grapeleaves=element["grapeleaves"]),
    )
    ke.run()
    pass

def getSweets(elementSweets):
    element = elementSweets
    ke = ChooseSweets()
    ke.reset()
    ke.declare(
        Sweets(creamCheese=element["creamCheese"]),
        Sweets(orange=element["orange"]),
        Sweets(apple=element["apple"]),
        Sweets(lemon=element["lemon"]),
        Sweets(carrots=element["carrots"]),
        Sweets(apricot=element["apricot"]),
        Sweets(semolina=element["semolina"]),
        Sweets(coffee=element["coffee"]),
        Sweets(chocolate=element["chocolate"]),
        Sweets(pineapple=element["pineapple"]),
        Sweets(blueberry=element["blueberry"]),
        Sweets(strawberry=element["strawberry"]),
        Sweets(mango=element["mango"]),
        Sweets(kunafa=element["kunafa"]),
        Sweets(ghee=element["ghee"]),
        Sweets(cream=element["cream"]),
        Sweets(flour=element["flour"]),
        Sweets(butter=element["butter"]),
        Sweets(cacao=element["cacao"]),
        Sweets(egg=element["egg"]),
        Sweets(oil=element["oil"]),
        Sweets(milk=element["milk"]),
        Sweets(yogurt=element["yogurt"]),
    )
    ke.run()
    pass

def getFoodBreakfast(elementFood):
    element = elementFood
    ke = ChooseEastren_Food()
    ke.reset()
    ke.declare(

        BreakfastEastren_Food(pasta=element["pasta"]),
        BreakfastEastren_Food(strawberryjam=element["strawberry jam"]),
        BreakfastEastren_Food(cheese=element["cheese"]),
        BreakfastEastren_Food(potato=element["potato"]),
        BreakfastEastren_Food(olive=element["olive"]),
        BreakfastEastren_Food(chickpeas=element["chickpeas"]),
        BreakfastEastren_Food(oil=element["oil"]),
        BreakfastEastren_Food(tomatojam=element["tomato jam"]),
        BreakfastEastren_Food(bread=element["bread"]),
        BreakfastEastren_Food(goth=element["goth"]),
        BreakfastEastren_Food(foul=element["foul"]),
        BreakfastEastren_Food(eggs=element["eggs"]),
        BreakfastEastren_Food(blackchocolate=element["black chocolate"]),
        BreakfastEastren_Food(whitechocolate=element["white chocolate"]),
        BreakfastEastren_Food(apricotjam=element["apricot jam"]),
        BreakfastEastren_Food(figsjam=element["figs jam"]),
        BreakfastEastren_Food(grapejam=element["grape jam"]),
        BreakfastEastren_Food(corneflakes=element["corne flakes"]),
        BreakfastEastren_Food(milk=element["milk"]),
        BreakfastEastren_Food(toast=element["toast"]),
        BreakfastEastren_Food(honey=element["honey"]),
        BreakfastEastren_Food(indomie=element["indomie"]),
        BreakfastEastren_Food(eggplant=element["eggplant"]),
        BreakfastEastren_Food(rosary=element["rosary"]),
        BreakfastEastren_Food(tahina=element["tahina"]),
        BreakfastEastren_Food(yogurt=element["yogurt"]),
        BreakfastEastren_Food(whitecheese=element["white cheese"]),
        BreakfastEastren_Food(yellowcheese=element["yellow cheese"]),
        BreakfastEastren_Food(thyme=element["thyme"]),
        BreakfastEastren_Food(cannedmeat=element["canned meat"]),

    )
    ke.run()
    pass

def getFoodDinner(elementFood):
    element = elementFood
    ke = ChooseEastren_Food()
    ke.reset()
    ke.declare(
        LunchEastren_Food(rice=element["rice"]),
        LunchEastren_Food(burger=element["burger"]),
        LunchEastren_Food(meat=element["meat"]),
        LunchEastren_Food(chicken=element["chicken"]),
        LunchEastren_Food(peas=element["peas"]),
        LunchEastren_Food(beans=element["beans"]),
        LunchEastren_Food(yogurt=element["yogurt"]),
        LunchEastren_Food(fish=element["fish"]),
        LunchEastren_Food(tomato=element["tomato"]),
        LunchEastren_Food(flour=element["flour"]),
        LunchEastren_Food(oil=element["oil"]),
        LunchEastren_Food(goth=element["goth"]),
        LunchEastren_Food(cools=element["cools"]),
        LunchEastren_Food(tomatocystom=element["tomato jam"]),
        LunchEastren_Food(cheese=element["cheese"]),
        LunchEastren_Food(onion=element["onion"]),
        LunchEastren_Food(eggplant=element["eggplant"]),
        LunchEastren_Food(potato=element["potato"]),
        LunchEastren_Food(mulukhiyah=element["mulukhiyah"]),
        LunchEastren_Food(grapeleaves=element["grape leaves"]),
        LunchEastren_Food(plugs=element["plugs"]),
        LunchEastren_Food(kosa=element["kosa"]),
        LunchEastren_Food(longyellowrice=element["long yellow rice"]),
        LunchEastren_Food(chickencutlets=element["chicken cutlets"]),
        LunchEastren_Food(flifla=element["flifla"]),
        LunchEastren_Food(bamia=element["bamia"]),

    )
    ke.run()
    pass

def getFoodLunch(elementFood):
    element = elementFood
    ke = ChooseEastren_Food()
    ke.reset()
    ke.declare(
        DinnerEastren_Food(pasta=element["pasta"]),
        DinnerEastren_Food(tomatojam=element["tomatojam"]),
        DinnerEastren_Food(strawberryjam=element["strawberry jam"]),
        DinnerEastren_Food(cheese=element["cheese"]),
        DinnerEastren_Food(potato=element["potato"]),
        # DinnerEastren_Food(brick=element["brick"]),
        DinnerEastren_Food(olive=element["olive"]),
        DinnerEastren_Food(chickpeas=element["chickpeas"]),
        DinnerEastren_Food(oil=element["oil"]),
        DinnerEastren_Food(tomatocystom=element["tomato jam"]),
        DinnerEastren_Food(bread=element["bread"]),
        DinnerEastren_Food(goth=element["goth"]),
        DinnerEastren_Food(foul=element["foul"]),
        DinnerEastren_Food(eggs=element["eggs"]),
        DinnerEastren_Food(blackchocolate=element["black chocolate"]),
        DinnerEastren_Food(whitechocolate=element["white chocolate"]),
        DinnerEastren_Food(apricotjam=element["apricot jam"]),
        DinnerEastren_Food(figsjam=element["figs jam"]),
        DinnerEastren_Food(grapejam=element["grape jam"]),
        DinnerEastren_Food(corneflakes=element["corne flakes"]),
        DinnerEastren_Food(milk=element["milk"]),
        DinnerEastren_Food(toast=element["toast"]),
        DinnerEastren_Food(honey=element["honey"]),
        DinnerEastren_Food(indomie=element["indomie"]),
        DinnerEastren_Food(eggplant=element["eggplant"]),
        DinnerEastren_Food(rosary=element["rosary"]),
        DinnerEastren_Food(tahina=element["tahina"]),
        DinnerEastren_Food(yogurt=element["yogurt"]),
        DinnerEastren_Food(whitecheese=element["white cheese"]),
        DinnerEastren_Food(yellowcheese=element["yellow cheese"]),
        DinnerEastren_Food(thyme=element["thyme"]),
        DinnerEastren_Food(cannedmeat=element["canned meat"]),
        DinnerEastren_Food(flour=element["flour"]),

    )
    ke.run()
    pass

def detectionFoodTable(type,elementSweets,elementFood,elementDrinks,elementAppetizer):
    getSweets(elementSweets)
    resultSweets = []
    if os.path.exists("Data Files/sweetsOutput.txt"):
        readfile = open("Data Files/sweetsOutput.txt", "r",encoding="utf-8")
        num = 1
        for line in readfile:
            if(num <= 1):
                line.replace('\n', '')
                resultSweets.append(line.replace('\n', ''))
                num = num + 1
                pass
        readfile.close()

    getDrinks(elementDrinks)
    resultDrinks = []
    if os.path.exists("Data Files/drinkOutput.txt"):
        readfile = open("Data Files/drinkOutput.txt", "r", encoding="utf-8")
        num = 1
        for line in readfile:
            if (num <= 1):
                line.replace('\n', '')
                resultDrinks.append(line.replace('\n', ''))
                num = num + 1
                pass
        readfile.close()


    getAppetizer(elementAppetizer)
    resultAppetizer = []
    if os.path.exists("Data Files/appetizerOutput.txt"):
        readfile = open("Data Files/appetizerOutput.txt", "r", encoding="utf-8")
        num = 1
        for line in readfile:
            if (num <= 3):
                line.replace('\n', '')
                resultAppetizer.append(line.replace('\n', ''))
                num = num + 1
                pass
        readfile.close()

    if(type == 1):
        getFoodBreakfast(elementFood)
        pass

    elif(type == 2):
        getFoodDinner(elementFood)
        pass

    elif(type == 3):
        getFoodLunch(elementFood)
        pass

    resultFood = []
    if os.path.exists("Data Files/orientalOutput.txt"):
        readfile = open("Data Files/orientalOutput.txt", "r", encoding="utf-8")
        num = 1
        for line in readfile:
            if (((type == 1) & (num <= 10)) | ((type == 2) & (num <= 3)) | ((type == 3) & (num <= 10))):
                line.replace('\n', '')
                resultFood.append(line.replace('\n', ''))
                num = num + 1
                pass
        readfile.close()
        pass

    totalResult ={
        "drinks":resultDrinks,
        "food":resultFood,
        "appetizer":resultAppetizer,
        "sweets":resultSweets
    }

    file = open("Data Files/result.txt", "a", encoding="utf-8")
    file.write(str(totalResult)+'\n')

    pass

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     deleteAllFile()
#     if os.path.exists("Data Files/result.txt"):
#         os.remove("Data Files/result.txt")
#         # print("done")
#     else:
#         print("The file does not exist")
#     detectionFoodTable(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
