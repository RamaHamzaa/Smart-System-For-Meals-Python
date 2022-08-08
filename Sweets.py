from experta import *
import os

class Sweets(Fact):  # For all
    pass

def writeOnFile(food):
    # if os.path.exists("Data Files/sweetsOutput.txt"):
    #     os.remove("Data Files/sweetsOutput.txt")
    #     # print("done")
    # else:
    #     print("The file does not exist")

    file = open("Data Files/sweetsOutput.txt", "a",encoding="utf-8")
    file.write(food+'\n')
    pass

class ChooseSweets(KnowledgeEngine):

    @Rule(Fact(start="yes"))
    def action1(self):
        element = {
            "carrots" : True ,
            "flour" : True ,
            "apricot" : True ,
            "lemon" : True ,
            "butter" : True ,
            "chocolate" : True ,
            "cacao" : True ,
            "egg" : True ,
            "oil" : True ,
            "kunafa" : True ,
            "ghee" : True ,
            "cream" : True ,
            "mango" : True ,
            "strawberry" : True ,
            "blueberry" : True ,
            "pineapple" : True ,
            "creamCheese" : True ,
            "semolina" : True ,
            "milk" : True ,
            "coffee" : True ,
            "yogurt" : True ,
            "apple" : True ,
            "orange" : True
        }

        self.declare(
            Sweets(creamCheese = element["creamCheese"]),
            Sweets(orange = element["orange"]),
            Sweets(apple = element["apple"]),
            Sweets(lemon = element["lemon"]),
            Sweets(carrots = element["carrots"]),
            Sweets(apricot = element["apricot"]),
            Sweets(semolina = element["semolina"]),
            Sweets(coffee = element["coffee"]),
            Sweets(chocolate = element["chocolate"]),
            Sweets(pineapple = element["pineapple"]),
            Sweets(blueberry = element["blueberry"]),
            Sweets(strawberry = element["strawberry"]),
            Sweets(mango = element["mango"]),
            Sweets(kunafa = element["kunafa"]),
            Sweets(ghee = element["ghee"]),
            Sweets(cream = element["cream"]),
            Sweets(flour = element["flour"]),
            Sweets(butter = element["butter"]),
            Sweets(cacao = element["cacao"]),
            Sweets(egg = element["egg"]),
            Sweets(oil = element["oil"]),
            Sweets(milk = element["milk"]),
            Sweets(yogurt = element["yogurt"]),
        )
        pass

    @Rule(AND(Sweets(flour = True),Sweets(butter = True),Sweets(cacao = True),Sweets(egg = True)),salience= 4)
    def action2(self):
        writeOnFile("كيكة الشوكولا السائلة")
        print("كيكة الشوكولا السائلة")
        pass

    @Rule(AND(Sweets(egg = True),Sweets(flour = True),Sweets(oil = True)),salience= 3)
    def action3(self):
        writeOnFile("الكيك الاسفنجي")
        print("الكيك الاسفنجي")
        pass

    @Rule(AND(Sweets(kunafa = True),Sweets(ghee = True),Sweets(cream = True)),salience= 3)
    def action4(self):
        writeOnFile("الكنافة السريعة المحشية بالقشطة")
        print("الكنافة السريعة المحشية بالقشطة")
        pass

    @Rule(AND(Sweets(mango = True),Sweets(strawberry = True),Sweets(blueberry = True),Sweets(pineapple = True)),salience= 4)
    def action5(self):
        writeOnFile("سلطة فواكه بالمانجا")
        print("سلطة فواكه بالمانجا")
        pass

    @Rule(AND(Sweets(creamCheese = True),Sweets(cream  = True),Sweets(milk = True)),salience= 3)
    def action6(self):
        writeOnFile("حلوى الكاسات")
        print("حلوى الكاسات")
        pass

    @Rule(AND(Sweets(coffee = True),Sweets(creamCheese = True),Sweets(chocolate = True)),salience= 3)
    def action7(self):
        writeOnFile("حلو القهوة والشوكولا")
        print("حلو القهوة والشوكولا")
        pass

    @Rule(AND(Sweets(butter = True),Sweets(flour = True),Sweets(egg = True),Sweets(apricot = True)),salience= 4)
    def action8(self):
        writeOnFile("تشيز كيك الشوكولاته")
        print("تشيز كيك الشوكولاته")
        pass

    @Rule(AND(Sweets(egg = True),Sweets(flour = True),Sweets(milk = True),Sweets(cacao = True),
              Sweets(oil = True),Sweets(creamCheese = True),Sweets(chocolate = True)),salience= 7)
    def action9(self):
        writeOnFile("كيك الكريب")
        print("كيك الكريب")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(egg = True),Sweets(butter = True)),salience= 3)
    def action10(self):
        writeOnFile("أصابع البتيفور")
        print("أصابع البتيفور")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(oil = True),Sweets(butter = True)),salience= 3)
    def action11(self):
        writeOnFile("غريبة تركية")
        print("غريبة تركية")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(butter = True),Sweets(egg = True),Sweets(milk = True)),salience= 4)
    def action12(self):
        writeOnFile("بتيفور محشي")
        print("بتيفور محشي")
        pass

    @Rule(AND(Sweets(carrots = True),Sweets(flour = True),Sweets(egg = True),Sweets(oil = True),
              Sweets(milk = True),Sweets(yogurt = True)),salience= 6)
    def action13(self):
        writeOnFile("كب كيك الجزر")
        print("كب كيك الجزر")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(egg = True),Sweets(milk = True),Sweets(oil = True),Sweets(apple = True)),salience= 5)
    def action14(self):
        writeOnFile("كيكة محشوة بالتفاح")
        print("كيكة محشوة بالتفاح")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(butter = True),Sweets(creamCheese = True),Sweets(egg = True),
              Sweets(lemon = True)),salience= 5)
    def action15(self):
        writeOnFile("كيكات ليمون صغيرة")
        print("كيكات ليمون صغيرة")
        pass

    @Rule(AND(Sweets(milk = True),Sweets(lemon = True),Sweets(flour = True),Sweets(cacao = True),
              Sweets(egg = True),Sweets(oil = True),Sweets(butter = True),Sweets(creamCheese = True)),salience= 8)
    def action16(self):
        writeOnFile("تورتة الكاكاو مع كريمة الكاكاو")
        print("تورتة الكاكاو مع كريمة الكاكاو")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(egg = True),Sweets(oil = True),Sweets(butter = True),Sweets(milk = True)),salience= 5)
    def action17(self):
        writeOnFile("كب كيك فليبيني")
        print("كب كيك فليبيني")
        pass

    @Rule(AND(Sweets(butter = True),Sweets(egg = True),Sweets(flour = True),Sweets(milk = True),Sweets(strawberry = True),
              Sweets(blueberry = True)),salience= 6)
    def action18(self):
        writeOnFile("تارت الفواكه")
        print("تارت الفواكه")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(cacao = True),Sweets(egg = True),Sweets(oil = True),Sweets(butter = True),
              Sweets(chocolate = True)),salience= 6)
    def action19(self):
        writeOnFile("كيكة شوكولاتة بالزيت")
        print("كيكة شوكولاتة بالزيت")
        pass

    @Rule(AND(Sweets(butter = True),Sweets(creamCheese = True),Sweets(yogurt = True),Sweets(egg = True)),salience= 4)
    def action20(self):
        writeOnFile("ميني تشيز كيك")
        print("ميني تشيز كيك")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(cacao = True),Sweets(butter = True),Sweets(egg = True),Sweets(yogurt = True)),salience=5)
    def action21(self):
        writeOnFile("كيك الكاكاو")
        print("كيك الكاكاو")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(ghee =True)),salience= 2)
    def action22(self):
        writeOnFile("غريبة")
        print("غريبة")
        pass

    @Rule(Sweets(semolina = True),salience= 1)
    def action23(self):
        writeOnFile("حلاوة السميد الملونة")
        print("حلاوة السميد الملونة")
        pass

    @Rule(AND(Sweets(strawberry = True),Sweets(chocolate = True)),salience= 2)
    def action24(self):
        writeOnFile("فراولة بالشوكولاتة")
        print("فراولة بالشوكولاتة")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(yogurt = True),Sweets(lemon = True)),salience=3)
    def action25(self):
        writeOnFile("لقمة القاضي")
        print("لقمة القاضي")
        pass

    @Rule(AND(Sweets(lemon = True),Sweets(strawberry = True)),salience=2)
    def action26(self):
        writeOnFile("مربى الفراولة")
        print("مربى الفراولة")
        pass

    @Rule(AND(Sweets(orange = True),Sweets(egg = True),Sweets(flour = True),Sweets(oil = True)),salience=4)
    def action27(self):
        writeOnFile("كيك البرتقالة")
        print("كيك البرتقالة")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(butter = True)),salience=2)
    def action28(self):
        writeOnFile("بسكويت العشر دقائق")
        print("بسكويت العشر دقائق")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(butter = True),Sweets(egg = True)),salience=3)
    def action29(self):
        writeOnFile("بسكويت بالزبدة")
        print("بسكويت بالزبدة")
        pass

    @Rule(AND(Sweets(butter = True),Sweets(cacao = True),Sweets(coffee= True),Sweets(flour = True),
              Sweets(milk = True)),salience=5)
    def action30(self):
        writeOnFile("بسكويت القهوة")
        print("بسكويت القهوة")
        pass

    @Rule(AND(Sweets(flour = True),Sweets(egg = True),Sweets(butter = True),Sweets(milk = True),
              Sweets(lemon = True),Sweets(strawberry = True)),salience=6)
    def action31(self):
        writeOnFile("وافل بصلصة الفراولة")
        print("وافل بصلصة الفراولة")
        pass

    pass

# ke = ChooseSweets()
# ke.reset()
# f = Fact(start="yes")
# ke.declare(f)
# ke.run()