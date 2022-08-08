from experta import *

def writeOnFile(food):
    # if os.path.exists("Data Files/sweetsOutput.txt"):
    #     os.remove("Data Files/sweetsOutput.txt")
    #     # print("done")
    # else:
    #     print("The file does not exist")

    file = open("Data Files/appetizerOutput.txt", "a",encoding="utf-8")
    file.write(food+'\n')
    pass

class Appetizer(Fact):  # for all
    pass

class BreakfastDrinks(Fact):  # وجبة الافطار
    pass

class LunchDrinks(Fact):  # وجبة الغداء
    pass

class DinnerDrinks(Fact):  # وجبة العشاء
    pass


class ChooseAppetizer(KnowledgeEngine):
    @Rule(Fact(start="yes"))
    def action1(self):
        element = {
            "watercrees" : True ,
            "sumac": True ,
            "gourd" : True ,
            "eggs" : True ,
            "tomato" : True ,
            "shrimp" : True ,
            "cuokumbber" : True ,
            "spinach" : True ,
            "watermelon" : True ,
            "cheese" : True ,
            "potato" : True ,
            "parsley" : True ,
            "yogurt" : True ,
            "corn" : True ,
            "venus" : True ,
            "mashroom" : True ,
            "chicken" : True ,
            "ozyychip" : True ,
            "eggplant" : True ,
            "tahina" : True ,
            "cauliflower" : True ,
            "garlic" : True,
            "chickpeas": True,
            "meat": True,
            "lemon": True,
            "flour": True,
            "beard": True,
            "beans": True,
            "redpepper": True,
            "beet": True,
            "walnut": True,
            "magi": True,
            "lentil": True,
            "grapeleaves": True,
        }

        self.declare(
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
        pass

    @Rule(AND(Appetizer(watercrees=True), Appetizer(sumac=True)),salience=2)
    def action2(self):
        writeOnFile("سلطة الجرجير بالسماق")
        print("سلطة الجرجير بالسماق")
        pass

    @Rule(AND(Appetizer(gourd=True),Appetizer(watercrees=True)), salience=2)
    def action3(self):
        writeOnFile("سلطة قرع مشوي")
        print("سلطة قرع مشوي")
        pass

    @Rule(AND(Appetizer(eggs=True), Appetizer(tomato=True)),salience=2)
    def action4(self):
        writeOnFile("سلطة خضار بالبيض المسلوق")
        print("سلطة خضار بالبيض المسلوق")
        pass

    @Rule(Appetizer(shrimp=True), salience=1)
    def action5(self):
        writeOnFile("سلطة الجمبري بالخضار")
        print("سلطة الجمبري بالخضار")
        pass

    @Rule(AND(Appetizer(tomato=True),Appetizer(spinach=True),Appetizer(cuokumbber=True)), salience=3)
    def action6(self):
        writeOnFile("تبولة السبانخ")
        print("تبولة السبانخ")
        pass

    @Rule(AND(Appetizer(watermelon=True),Appetizer(cheese=True)), salience=2)
    def action7(self):
        writeOnFile("سلطة البطيخ بجبن الحلوم والنعنع")
        print("سلطة البطيخ بجبن الحلوم والنعنع")
        pass

    @Rule(AND( Appetizer(potato=True), Appetizer(parsley=True)),salience=2)
    def action8(self):
        writeOnFile("سلطة البطاطا بالقدونس")
        print("سلطة البطاطا بالقدونس")
        pass

    @Rule(Appetizer(corn=True), salience=1)
    def action9(self):
        writeOnFile("سلطة الذرة المشوية")
        print("سلطة الذرة المشوية")
        pass

    @Rule(AND(Appetizer(yogurt=True),Appetizer(cuokumbber=True)), salience=2)
    def action10(self):
        writeOnFile("سلطة خيار باللبن")
        print("سلطة خيار باللبن")
        pass

    @Rule(AND(Appetizer(potato=True),Appetizer(cheese=True)), salience=2)
    def action11(self):
        writeOnFile("كرات البطاطس الايطالية")
        print("كرات البطاطس الايطالية")
        pass

    @Rule(Appetizer(venus=True), salience=1)
    def action12(self):
        writeOnFile("زهرة بالفرن")
        print("زهرة بالفرن")
        pass

    @Rule(Appetizer(mashroom=True), salience=1)
    def action13(self):
        writeOnFile("مشروم سوتيه")
        print("مشروم سوتيه")
        pass

    @Rule(AND(Appetizer(chicken=True),Appetizer(ozyychip=True)), salience=2)
    def action14(self):
        writeOnFile("سبرينغ رول الدجاج")
        print("سبرينغ رول الدجاج")
        pass

    @Rule(AND( Appetizer(eggplant=True),Appetizer(tahina=True)),salience=2)
    def action15(self):
        writeOnFile("المتبل اللبناني")
        print("المتبل اللبناني")
        pass

    @Rule(AND(Appetizer(cauliflower=True), Appetizer(garlic=True)), salience=2)
    def action16(self):
        writeOnFile("قرنبيط مهروس بالثوم")
        print("قرنبيط مهروس بالثوم")
        pass

    @Rule(AND(Appetizer(meat=True), Appetizer(chickpeas=True)), salience=2)
    def action17(self):
        writeOnFile("حمص باللحم المحمر")
        print("حمص باللحم المحمر")
        pass


    @Rule( Appetizer(lemon=True), salience=1)
    def action18(self):
        writeOnFile("مخلل الليمون بحبة البركة")
        print("مخلل الليمون بحبة البركة")
        pass

    @Rule(Appetizer(cuokumbber=True), salience=1)
    def action19(self):
        writeOnFile("مخلل الخيار")
        print("مخلل الخيار")
        pass

    @Rule(AND(Appetizer(tomato=True), Appetizer(flour=True)), salience=2)
    def action20(self):
        writeOnFile("بيتزا")
        print("بيتزا")
        pass

    @Rule(Appetizer(beans=True), salience=1)
    def action21(self):
        writeOnFile("فول مقلى")
        print("فول مقلى")
        pass

    @Rule(Appetizer(chickpeas=True), salience=1)
    def action22(self):
        writeOnFile("الحمص الناعم")
        print("الحمص الناعم")
        pass

    @Rule(Appetizer(redpepper=True), salience=1)
    def action23(self):
        writeOnFile("المحمرة")
        print("المحمرة")
        pass

    @Rule(Appetizer(beet=True), salience=1)
    def action24(self):
        writeOnFile("متبل الشوندر")
        print("متبل الشوندر")
        pass

    @Rule(AND(Appetizer(eggplant=True),Appetizer(walnut=True)), salience=2)
    def action25(self):
        writeOnFile("المكدوس")
        print("المكدوس")
        pass

    @Rule(AND(Appetizer(beard=True), Appetizer(chickpeas=True)), salience=2)
    def action26(self):
        writeOnFile("تسقية")
        print("تسقية")
        pass

    @Rule(Appetizer(grapeleaves=True), salience=1)
    def action27(self):
        writeOnFile("اليالنجي")
        print("اليالنجي")
        pass

    @Rule(Appetizer(lentil=True), salience=1)
    def action28(self):
        writeOnFile("شوربة العدس")
        print("شوربة العدس")
        pass

    @Rule(Appetizer(meat=True), salience=1)
    def action29(self):
        writeOnFile("شوربة اللحم")
        print("شوربة اللحم")
        pass

    @Rule(Appetizer(magi=True), salience=1)
    def action30(self):
        writeOnFile("شوربة الماجي")
        print("شوربة الماجي")
        pass
    pass

# ke = ChooseAppetizer()
# ke.reset()
# f = Fact(start="yes")
# ke.declare(f)
# ke.run()

