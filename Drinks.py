from experta import *
import os

class Drinks(Fact):  # For all
    pass

def writeOnFile(food):
    # if os.path.exists("Data Files/drinkOutput.txt"):
    #     os.remove("Data Files/drinkOutput.txt")
    #     # print("done")
    # else:
    #     print("The file does not exist")

    file = open("Data Files/drinkOutput.txt", "a",encoding="utf-8")
    file.write(food+'\n')
    pass

class ChooseDrinks(KnowledgeEngine):
    @Rule(Fact(start="yes"))
    def action1(self):
        element = {
            "cacao" : True ,
            "coffee": True ,
            "milk" : True ,
            "nescafe" : True ,
            "lemon" : True ,
            "mint" : True ,
            "apple" : True ,
            "banana" : True ,
            "orange" : True ,
            "honey" : True ,
            "strawberry" : True ,
            "mango" : True ,
            "avocado" : True ,
            "melon" : True ,
            "carrots" : True ,
            "cranberry" : True ,
            "watermelon" : True ,
            "kiwi" : True ,
            "pineapple" : True ,
            "tea" : True ,
            "oats" : True ,
            "cream" : True
        }

        self.declare(
            Drinks(cacao = element["cacao"]),
            Drinks(coffee = element["coffee"]),
            Drinks(milk = element["milk"]),
            Drinks(nescafe = element["nescafe"]),
            Drinks(lemon = element["lemon"]),
            Drinks(mint = element["mint"]),
            Drinks(apple = element["apple"]),
            Drinks(banana = element["banana"]),
            Drinks(orange = element["orange"]),
            Drinks(honey = element["honey"]),
            Drinks(strawberry = element["strawberry"]),
            Drinks(mango = element["mango"]),
            Drinks(avocado = element["avocado"]),
            Drinks(melon = element["melon"]),
            Drinks(carrots = element["carrots"]),
            Drinks(cranberry = element["cranberry"]),
            Drinks(watermelon = element["watermelon"]),
            Drinks(kiwi = element["kiwi"]),
            Drinks(pineapple = element["pineapple"]),
            Drinks(oats = element["oats"]),
            Drinks(cream = element["cream"]),
            Drinks(tea = element["tea"]),
        )
        pass

    @Rule(Drinks(cacao = True),salience=1)
    def action2(self):
        writeOnFile("شوكولا حارة")
        print("شوكولا حارة")
        pass

    @Rule(Drinks(milk=True),salience= 1)
    def action3(self):
        writeOnFile("حليب")
        print("حليب")
        pass

    @Rule(AND(Drinks(cacao = True),Drinks(milk = True)),salience= 2)
    def action4(self):
        writeOnFile("حليب بالكاكاو")
        print("حليب بالكاكاو")
        pass

    @Rule(Drinks(lemon = True),salience= 1)
    def action5(self):
        writeOnFile("عصير ليمون")
        print("عصير ليمون")
        pass

    @Rule(AND(Drinks(lemon = True),Drinks(mint = True)), salience= 2)
    def action6(self):
        writeOnFile("عصير ليمون بالنعنع")
        print("عصير ليمون بالنعنع")
        pass

    @Rule(Drinks(coffee = True),salience= 1)
    def action7(self):
        writeOnFile("قهوة")
        print("قهوة")
        pass

    @Rule(AND(Drinks(coffee = True),Drinks(milk = True)),salience= 2)
    def action8(self):
        writeOnFile("حليب بالقهوة")
        print("حليب بالقهوة")
        pass

    @Rule(AND(Drinks(apple = True),Drinks(orange = True),Drinks(honey = True),Drinks(banana = True),Drinks(milk = True)),salience=5)
    def action9(self):
        writeOnFile("عصير كوكتيل الفواكه")
        print("عصير كوكتيل الفواكه")
        pass

    @Rule(Drinks(nescafe = True),salience=1)
    def action10(self):
        writeOnFile("نيسكافيه")
        print("نيسكافيه")
        pass

    @Rule(AND(Drinks(nescafe = True),Drinks(milk = True)),salience=2)
    def action11(self):
        writeOnFile("حليب بالنيسكافيه")
        print("حليب بالنيسكافيه")
        pass

    @Rule(AND(Drinks(milk = True),Drinks(honey = True)),salience=2)
    def action12(self):
        writeOnFile("حليب مع عسل")
        print("حليب مع عسل")
        pass

    @Rule(AND(Drinks(strawberry = True),Drinks(mango = True),Drinks(avocado = True),Drinks(milk = True)),salience= 4)
    def action13(self):
        writeOnFile("كوكتيل العصائر بالحليب")
        print("كوكتيل العصائر بالحليب")
        pass

    @Rule(AND(Drinks(melon = True),Drinks(carrots = True),Drinks(orange = True)),salience= 3)
    def action14(self):
        writeOnFile("عصير الكوكتيل بالشمام")
        print("عصير الكوكتيل بالشمام")
        pass

    @Rule(AND(Drinks(cranberry = True),Drinks(lemon = True)),salience= 2)
    def action15(self):
        writeOnFile("كوكتيل التوت البري والليمون")
        print("كوكتيل التوت البري والليمون")
        pass

    @Rule(AND(Drinks(watermelon = True),Drinks(melon = True)),salience= 2)
    def action16(self):
        writeOnFile("كوكتيل الشمام والبطيخ")
        print("كوكتيل الشمام والبطيخ")
        pass

    @Rule(AND(Drinks(strawberry = True),Drinks(milk = True)),salience= 2)
    def action17(self):
        writeOnFile("كوكتيل الفراولة")
        print("كوكتيل الفراولة")
        pass

    @Rule(AND(Drinks(banana = True),Drinks(strawberry = True),Drinks(kiwi = True),Drinks(pineapple = True),
              Drinks(mango = True),Drinks(cacao = True),Drinks(cream = True),Drinks(honey = True)),salience= 8)
    def action18(self):
        writeOnFile("كوكتيل الفواكه بالعسل والقشطة")
        print("كوكتيل الفواكه بالعسل والقشطة")
        pass

    @Rule(Drinks(tea = True),salience= 1)
    def action19(self):
        writeOnFile("شاي")
        print("شاي")
        pass

    @Rule(Drinks(mint = True),salience= 1)
    def action20(self):
        writeOnFile("نعنع")
        print("نعنع")
        pass

    @Rule(AND(Drinks(lemon = True),Drinks(orange = True)),salience= 2)
    def action21(self):
        writeOnFile("كوكتيل مارغريتا")
        print("كوكتيل مارغريتا")
        pass

    @Rule(AND(Drinks(banana = True),Drinks(apple = True),Drinks(milk = True),Drinks(honey = True),
              Drinks(oats = True)),salience= 5)
    def action22(self):
        writeOnFile("كوكتيل الشوفان بالفواكه")
        print("كوكتيل الشوفان بالفواكه")
        pass

    @Rule(AND(Drinks(tea = True),Drinks(mint = True)),salience= 2)
    def action23(self):
        writeOnFile("شاي بالنعنع")
        print("شاي بالنعنع")
        pass

    @Rule(Drinks(strawberry = True),salience= 1)
    def action24(self):
        writeOnFile("عصير فراولة")
        print("عصير فراولة")
        pass

    @Rule(Drinks(orange = True),salience= 1)
    def action25(self):
        writeOnFile("عصير البرتقال")
        print("عصير البرتقال")
        pass

    @Rule(AND(Drinks(apple = True),Drinks(milk = True)),salience= 2)
    def action26(self):
        writeOnFile("كوكتيل التفاح")
        print("كوكتيل التفاح")
        pass

    @Rule(AND(Drinks(banana = True),Drinks(milk = True)),salience= 2)
    def action27(self):
        writeOnFile("كوكتيل الموز")
        print("كوكتيل الموز")
        pass

    @Rule(Drinks(mango = True),salience= 1)
    def action28(self):
        writeOnFile("عصير المانجا")
        print("عصير المانجا")
        pass

    @Rule(Drinks(kiwi = True),salience=1)
    def action29(self):
        writeOnFile("عصير الكيوي")
        print("عصير الكيوي")
        pass

    @Rule(Drinks(avocado = True),salience= 1)
    def action30(self):
        writeOnFile("عصير الافوكادو")
        print("عصير الافوكادو")
        pass

    @Rule(Drinks(carrots = True),salience= 1)
    def action31(self):
        writeOnFile("عصير الجزر")
        print("عصير الجزر")
        pass

    pass

# ke = ChooseDrinks()
# ke.reset()
# f = Fact(start="yes")
# ke.declare(f)
# ke.run()