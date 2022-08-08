from experta import *

def writeOnFile(food):
    # if os.path.exists("Data Files/sweetsOutput.txt"):
    #     os.remove("Data Files/sweetsOutput.txt")
    #     # print("done")
    # else:
    #     print("The file does not exist")

    file = open("Data Files/orientalOutput.txt", "a",encoding="utf-8")
    file.write(food+'\n')
    pass

class BreakfastEastren_Food(Fact):  # وجبة الافطار
    pass


class LunchEastren_Food(Fact):  # وجبة الغداء
    pass


class DinnerEastren_Food(Fact):  # وجبة العشاء
    pass


class ChooseEastren_Food(KnowledgeEngine):

    @Rule(Fact(start="yes"))
    def action1(self):
        print("1- Breakfast Meal  ...")
        print("2- Lunch Meal  ...")
        print("3- Dinner Meal ...")

        choose = input("Enter your Choose Type meal :")
        self.declare(Fact(choose=int(choose)))
        pass

    @Rule(Fact(choose=1))
    def action2(self):
        element = {

            "foul": True,
            "tomato": True,
            "onion": True,
            "flour": True,
            "pasta": True,
            "potato": True,
            "chickpeas": True,
            "cheese": True,
            "strawberry jam": True,
            "oil": True,
            "tomato jam": True,
            "bread": True,
            "goth": True,
            "olive": True,
            "eggs": True,
            "black chocolate": True,
            "white chocolate": True,
            "apricot jam": True,
            "figs jam": True,
            "grape jam": True,
            "corne flakes": True,
            "milk": True,
            "toast": True,
            "honey": True,
            "indomie": True,
            "eggplant": True,
            "rosary": True,
            "tahina": True,
            "yogurt": True,
            "white cheese": True,
            "yellow cheese": True,
            "thyme": True,
            "canned meat": True,

        }
        self.declare(

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
        pass

    @Rule(AND(BreakfastEastren_Food(pasta=True), BreakfastEastren_Food(tomatojam=True)), salience=2)
    def action3(self):
        writeOnFile("معكرونة بصلصة البندورة")
        print("معكرونة بصلصة البندورة")
        pass

    @Rule(AND(BreakfastEastren_Food(potato=True), BreakfastEastren_Food(oil=True)), salience=2)
    def action4(self):
        writeOnFile("بطاطا مقلية")
        print("بطاطا مقلية")
        pass

    @Rule(AND(BreakfastEastren_Food(strawberryjam=True), BreakfastEastren_Food(bread=True)), salience=2)
    def action5(self):
        writeOnFile("ساندويش مربى الفروالة")
        print("ساندويش مربى الفروالة")
        pass

    @Rule(AND(BreakfastEastren_Food(cheese=True), BreakfastEastren_Food(bread=True)), salience=2)
    def action6(self):
        writeOnFile("ساندويش الجبن")
        print("ساندويش الجبن")
        pass

    @Rule(AND(BreakfastEastren_Food(olive=True), BreakfastEastren_Food(bread=True)), salience=2)
    def action7(self):
        writeOnFile("ساندويش الزيتون")
        print("ساندويش الزيتون")
        pass

    @Rule(AND(BreakfastEastren_Food(chickpeas=True), BreakfastEastren_Food(oil=True), BreakfastEastren_Food(goth=True)),
          salience=3)
    def action8(self):
        writeOnFile("حمص متبل بالزيت")
        print("حمص متبل بالزيت")
        pass

    @Rule(AND(BreakfastEastren_Food(foul=True), BreakfastEastren_Food(oil=True), BreakfastEastren_Food(goth=True)),
          salience=3)
    def action9(self):
        writeOnFile("فول متبل بالزيت")
        print("فول متبل بالزيت")
        pass

    @Rule(AND(BreakfastEastren_Food(pasta=True), BreakfastEastren_Food(cheese=True)), salience=2)
    def action10(self):
        writeOnFile("معكرونة بالجبن")
        print("معكرونة بالجبن")
        pass

    @Rule(BreakfastEastren_Food(eggs=True), salience=1)
    def action11(self):
        writeOnFile("بيض مسلوق")
        print("بيض مسلوق")
        pass

    @Rule(AND(BreakfastEastren_Food(eggs=True), BreakfastEastren_Food(oil=True)), salience=2)
    def action12(self):
        writeOnFile("بيض مقلي")
        print("بيض مقلي")
        pass

    @Rule(BreakfastEastren_Food(apricotjam=True), salience=1)
    def action13(self):
        writeOnFile("مربى المشمش")
        print("مربى المشمش")
        pass

    @Rule(BreakfastEastren_Food(blackchocolate=True), salience=1)
    def action14(self):
        writeOnFile("شوكولا سوداء")
        print("شوكولا سوداء")
        pass

    @Rule(BreakfastEastren_Food(whitechocolate=True), salience=1)
    def action15(self):
        writeOnFile("شوكولا بيضاء")
        print("شوكولا بيضاء")
        pass

    @Rule(BreakfastEastren_Food(figsjam=True), salience=1)
    def action16(self):
        writeOnFile("مربى التين")
        print("مربى التين")
        pass

    @Rule(BreakfastEastren_Food(grapejam=True), salience=1)
    def action17(self):
        writeOnFile("مربى العنب")
        print("مربى العنب")
        pass

    @Rule(AND(BreakfastEastren_Food(corneflakes=True), BreakfastEastren_Food(milk=True)), salience=2)
    def action18(self):
        writeOnFile("كورنفليكس مع الحليب")
        print("كورنفليكس مع الحليب")
        pass

    @Rule(BreakfastEastren_Food(indomie=True), salience=1)
    def action19(self):
        writeOnFile("اندومي")
        print("اندومي")
        pass

    @Rule(AND(BreakfastEastren_Food(honey=True), BreakfastEastren_Food(toast=True)), salience=2)
    def action20(self):
        writeOnFile("توست مع العسل")
        print("توست مع العسل")
        pass

    @Rule(AND(BreakfastEastren_Food(eggplant=True), BreakfastEastren_Food(tahina=True)), salience=2)
    def action21(self):
        writeOnFile("متبل باذنجان")
        print("متبل باذنجان")
        pass

    @Rule(BreakfastEastren_Food(potato=True), salience=1)
    def action22(self):
        writeOnFile("بطاطا مسلوقة")
        print("بطاطا مسلوقة")
        pass

    @Rule(BreakfastEastren_Food(yogurt=True), salience=1)
    def action23(self):
        writeOnFile("لبن")
        print("لبن")
        pass

    @Rule(BreakfastEastren_Food(whitecheese=True), salience=1)
    def action24(self):
        writeOnFile("جبن ابيض")
        print("جبن ابيض")
        pass

    @Rule(BreakfastEastren_Food(yellowcheese=True), salience=1)
    def action25(self):
        writeOnFile("جبن اصفر")
        print("جبن اصفر")
        pass

    @Rule(BreakfastEastren_Food(rosary=True), salience=1)
    def action26(self):
        writeOnFile("مسبحة")
        print("مسبحة")
        pass

    @Rule(BreakfastEastren_Food(chickpeas=True), BreakfastEastren_Food(bread=True), salience=2)
    def action27(self):
        writeOnFile("فتة حمص")
        print("فتة حمص")
        pass

    @Rule(AND(BreakfastEastren_Food(thyme=True), BreakfastEastren_Food(flour=True)), salience=2)
    def action28(self):
        writeOnFile("مناقيش الزعتر")
        print("مناقيش الزعتر")
        pass

    @Rule(BreakfastEastren_Food(chickpeas=True), salience=1)
    def action29(self):
        writeOnFile("فلافل")
        print("فلافل")
        pass

    @Rule(BreakfastEastren_Food(cannedmeat=True), salience=1)
    def action30(self):
        writeOnFile("مرتديلا")
        print("مرتديلا")
        pass

    @Rule(Fact(choose=2))
    def action31(self):
        element = {
            "rice": True,
            "meat": True,
            "chicken": True,
            "burger": True,
            "peas": True,
            "beans": True,
            "yogurt": True,
            "fish": True,
            "tomato": True,
            "eggplant": True,
            "onion": True,
            "flour": True,
            "flifla": True,
            "pasta": True,
            "potato": True,
            "chickpeas": True,
            "cheese": True,
            "cools": True,
            "mulukhiyah": True,
            "oil": True,
            "goth": True,
            "grape leaves": True,
            "plugs": True,
            "kosa": True,
            "long yellow rice": True,
            "chicken cutlets": True,
            "bamia": True,
            "tomato jam": True,

        }

        self.declare(
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
        pass

    @Rule(AND(LunchEastren_Food(rice=True), LunchEastren_Food(peas=True)), salience=2)
    def action32(self):
        writeOnFile("رز بالبازلاء")
        print("رز بالبازلاء")
        pass

    @Rule(AND(LunchEastren_Food(rice=True), LunchEastren_Food(tomatocystom=True), LunchEastren_Food(beans=True)),
          salience=3)
    def action33(self):
        writeOnFile("رز وفاصولياء")
        print("رز وفاصولياء")
        pass

    @Rule(AND(LunchEastren_Food(mulukhiyah=True), LunchEastren_Food(chicken=True), LunchEastren_Food(goth=True)),
          salience=3)
    def action34(self):
        writeOnFile("ملوخية بالدجاج")
        print("ملوخية بالدجاج")
        pass

    @Rule(AND(LunchEastren_Food(fish=True), LunchEastren_Food(oil=True)), salience=2)
    def action35(self):
        writeOnFile("سمك مقلي")
        print("سمك مقلي")
        pass

    @Rule(LunchEastren_Food(fish=True), salience=1)
    def action36(self):
        writeOnFile("سمك مشوي")
        print("سمك مشوي")
        pass

    @Rule(AND(LunchEastren_Food(yogurt=True), LunchEastren_Food(meat=True), LunchEastren_Food(onion=True)),
          salience=3)
    def action37(self):
        writeOnFile("شاكرية باللحم")
        print("شاكرية باللحم")
        pass

    @Rule(AND(LunchEastren_Food(flour=True), LunchEastren_Food(yogurt=True), LunchEastren_Food(meat=True)),
          salience=3)
    def action38(self):
        writeOnFile("شيشبرك")
        print("شيشبرك")
        pass

    @Rule(AND(LunchEastren_Food(cools=True), LunchEastren_Food(meat=True)), salience=2)
    def action39(self):
        writeOnFile("ملفوف اليخنة")
        print("ملفوف اليخنة")
        pass

    @Rule(AND(LunchEastren_Food(chicken=True), LunchEastren_Food(potato=True)), salience=2)
    def action40(self):
        writeOnFile("بطاطا بالفرن")
        print("بطاطا بالفرن")
        pass

    @Rule(AND(LunchEastren_Food(potato=True), LunchEastren_Food(burger=True)), salience=2)
    def action41(self):
        writeOnFile("برغل مع بطاطا")
        print("برغل مع بطاطا")
        pass

    @Rule(AND(LunchEastren_Food(meat=True), LunchEastren_Food(rice=True), LunchEastren_Food(eggplant=True)),
          salience=3)
    def action42(self):
        writeOnFile("مقلوبة الباذنجان")
        print("مقلوبة الباذنجان")
        pass

    @Rule(AND(LunchEastren_Food(grapeleaves=True), LunchEastren_Food(meat=True)), salience=2)
    def action43(self):
        writeOnFile("ورق عنب باللحم")
        print("ورق عنب باللحم")
        pass

    @Rule(AND(LunchEastren_Food(grapeleaves=True), LunchEastren_Food(plugs=True), LunchEastren_Food(tomato=True)),
          salience=3)
    def action44(self):
        writeOnFile("ورق عنب بالخضار")
        print("ورق عنب بالخضار")
        pass

    @Rule(AND(LunchEastren_Food(rice=True), LunchEastren_Food(chicken=True)), salience=2)
    def action45(self):
        writeOnFile("رز بالدجاج")
        print("رز بالدجاج")
        pass

    @Rule(AND(LunchEastren_Food(rice=True), LunchEastren_Food(meat=True), LunchEastren_Food(yogurt=True)),
          salience=3)
    def action46(self):
        writeOnFile("منسف أردني")
        print("منسف أردني")
        pass

    @Rule(AND(LunchEastren_Food(tomato=True), LunchEastren_Food(flifla=True), LunchEastren_Food(meat=True)),
          salience=3)
    def action47(self):
        writeOnFile("كواج البندورة")
        print("كواج البندورة")
        pass

    @Rule(AND(LunchEastren_Food(kosa=True), LunchEastren_Food(meat=True), LunchEastren_Food(tomatocystom=True)),
          salience=3)
    def action48(self):
        writeOnFile("محاشي")
        print("محاشي")
        pass

    @Rule(AND(LunchEastren_Food(chicken=True), LunchEastren_Food(oil=True)), salience=2)
    def action49(self):
        writeOnFile("كريسبي")
        print("كريسبي")
        pass

    @Rule(AND(LunchEastren_Food(beans=True), LunchEastren_Food(tomatocystom=True)), salience=2)
    def action50(self):
        writeOnFile("فاصولياء مع بندورة")
        print("فاصولياء مع بندورة")
        pass

    @Rule(AND(LunchEastren_Food(meat=True), LunchEastren_Food(tomato=True)), salience=2)
    def action51(self):
        writeOnFile("لحم بالفرن")
        print("لحم بالفرن")
        pass

    @Rule(AND(LunchEastren_Food(bamia=True), LunchEastren_Food(tomatocystom=True), LunchEastren_Food(meat=True)),
          salience=3)
    def action52(self):
        writeOnFile("بامياء مع مرق البندورة")
        print("بامياء مع مرق البندورة")
        pass

    @Rule(AND(LunchEastren_Food(beans=True), LunchEastren_Food(oil=True), LunchEastren_Food(tomato=True)),
          salience=3)
    def action53(self):
        writeOnFile("فاصولياء مقلاة بالزيت")
        print("فاصولياء مقلاة بالزيت")
        pass

    @Rule(LunchEastren_Food(tomato=True), LunchEastren_Food(burger=True), salience=2)
    def action54(self):
        writeOnFile("برغل بالبندورة")
        print("برغل بالبندورة")
        pass

    @Rule(AND(LunchEastren_Food(potato=True), LunchEastren_Food(tomato=True), LunchEastren_Food(eggplant=True)),
          salience=3)
    def action55(self):
        writeOnFile("الطاجن التونسي")
        print("الطاجن التونسي")
        pass

    @Rule(AND(LunchEastren_Food(flour=True), LunchEastren_Food(cheese=True)),
          salience=2)
    def action56(self):
        writeOnFile("معجنات بالجبن")
        print("معجنات بالجبن")
        pass

    @Rule(AND(LunchEastren_Food(flour=True), LunchEastren_Food(tomato=True)),
          salience=2)
    def action57(self):
        writeOnFile("بيتزا")
        print("بيتزا")
        pass

    @Rule(LunchEastren_Food(chickencutlets=True),
          salience=1)
    def action58(self):
        writeOnFile("شاورما")
        print("شاورما")
        pass

    @Rule(LunchEastren_Food(chicken=True),
          salience=1)
    def action59(self):
        writeOnFile("دجاج مشوي")
        print("دجاج مشوي")
        pass

    @Rule(AND(LunchEastren_Food(longyellowrice=True), LunchEastren_Food(tomato=True)),
          salience=2)
    def action60(self):
        writeOnFile("مندي")
        print("مندي")
        pass

    @Rule(Fact(choose=3))
    def action61(self):
        element = {

            "foul": True,
            "tomatojam": True,
            "tomato": True,
            "onion": True,
            "flour": True,
            "pasta": True,
            "potato": True,
            "chickpeas": True,
            "cheese": True,
            "strawberry jam": True,
            "oil": True,
            "tomato jam": True,
            "bread": True,
            "goth": True,
            "olive": True,
            "eggs": True,
            "black chocolate": True,
            "white chocolate": True,
            "apricot jam": True,
            "figs jam": True,
            "grape jam": True,
            "corne flakes": True,
            "milk": True,
            "toast": True,
            "honey": True,
            "indomie": True,
            "eggplant": True,
            "rosary": True,
            "tahina": True,
            "yogurt": True,
            "white cheese": True,
            "yellow cheese": True,
            "thyme": True,
            "canned meat": True,
        }

        self.declare(

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
        pass

    @Rule(AND(DinnerEastren_Food(pasta=True), DinnerEastren_Food(tomatojam=True)), salience=2)
    def action62(self):
        writeOnFile("معكرونة بمربى البندورة")
        print("معكرونة بمربى البندورة")
        pass

    @Rule(AND(DinnerEastren_Food(potato=True), DinnerEastren_Food(oil=True)), salience=2)
    def action63(self):
        writeOnFile("بطاطا مقلية")
        print("بطاطا مقلية")
        pass

    @Rule(AND(DinnerEastren_Food(strawberryjam=True), DinnerEastren_Food(bread=True)), salience=2)
    def action64(self):
        writeOnFile("ساندويش مربى الفروالة")
        print("ساندويش مربى الفروالة")
        pass

    @Rule(AND(DinnerEastren_Food(cheese=True), DinnerEastren_Food(bread=True)), salience=2)
    def action65(self):
        writeOnFile("ساندويش الجبن")
        print("ساندويش الجبن")
        pass

    @Rule(AND(DinnerEastren_Food(olive=True), DinnerEastren_Food(bread=True)), salience=2)
    def action66(self):
        writeOnFile("ساندويش الزيتون")
        print("ساندويش الزيتون")
        pass

    @Rule(AND(DinnerEastren_Food(chickpeas=True), DinnerEastren_Food(oil=True), DinnerEastren_Food(goth=True)),
          salience=3)
    def action67(self):
        writeOnFile("حمص متبل بالزيت")
        print("حمص متبل بالزيت")
        pass

    @Rule(AND(DinnerEastren_Food(foul=True), DinnerEastren_Food(oil=True), DinnerEastren_Food(goth=True)),
          salience=3)
    def action68(self):
        writeOnFile("فول متبل بالزيت")
        print("فول متبل بالزيت")
        pass

    @Rule(AND(DinnerEastren_Food(pasta=True), DinnerEastren_Food(cheese=True)), salience=2)
    def action69(self):
        writeOnFile("معكرونة بالجبن")
        print("معكرونة بالجبن")
        pass

    @Rule(DinnerEastren_Food(eggs=True), salience=1)
    def action70(self):
        writeOnFile("بيض مسلوق")
        print("بيض مسلوق")
        pass

    @Rule(AND(DinnerEastren_Food(eggs=True), DinnerEastren_Food(oil=True)), salience=2)
    def action71(self):
        writeOnFile("بيض مقلي")
        print("بيض مقلي")
        pass

    @Rule(DinnerEastren_Food(apricotjam=True), salience=1)
    def action72(self):
        writeOnFile("مربى المشمش")
        print("مربى المشمش")
        pass

    @Rule(DinnerEastren_Food(blackchocolate=True), salience=1)
    def action73(self):
        writeOnFile("شوكولا سوداء")
        print("شوكولا سوداء")
        pass

    @Rule(DinnerEastren_Food(whitechocolate=True), salience=1)
    def action74(self):
        writeOnFile("شوكولا بيضاء")
        print("شوكولا بيضاء")
        pass

    @Rule(DinnerEastren_Food(figsjam=True), salience=1)
    def action75(self):
        writeOnFile("مربى التين")
        print("مربى التين")
        pass

    @Rule(DinnerEastren_Food(grapejam=True), salience=1)
    def action76(self):
        writeOnFile("مربى العنب")
        print("مربى العنب")
        pass

    @Rule(AND(DinnerEastren_Food(corneflakes=True), DinnerEastren_Food(milk=True)), salience=2)
    def action77(self):
        writeOnFile("كورنفليكس مع الحليب")
        print("كورنفليكس مع الحليب")
        pass

    @Rule(DinnerEastren_Food(indomie=True), salience=1)
    def action78(self):
        writeOnFile("اندومي")
        print("اندومي")
        pass

    @Rule(AND(DinnerEastren_Food(honey=True), DinnerEastren_Food(toast=True)), salience=2)
    def action79(self):
        writeOnFile("توست مع العسل")
        print("توست مع العسل")
        pass

    @Rule(AND(DinnerEastren_Food(eggplant=True), DinnerEastren_Food(tahina=True)), salience=2)
    def action80(self):
        writeOnFile("متبل باذنجان")
        print("متبل باذنجان")
        pass

    @Rule(DinnerEastren_Food(potato=True), salience=1)
    def action81(self):
        writeOnFile("بطاطا مسلوقة")
        print("بطاطا مسلوقة")
        pass

    @Rule(DinnerEastren_Food(yogurt=True), salience=1)
    def action82(self):
        writeOnFile("لبن")
        print("لبن")
        pass

    @Rule(DinnerEastren_Food(whitecheese=True), salience=1)
    def action83(self):
        writeOnFile("جبن ابيض")
        print("جبن ابيض")
        pass

    @Rule(DinnerEastren_Food(yellowcheese=True), salience=1)
    def action84(self):
        writeOnFile("جبن اصفر")
        print("جبن اصفر")
        pass

    @Rule(DinnerEastren_Food(rosary=True), salience=1)
    def action85(self):
        writeOnFile("مسبحة")
        print("مسبحة")
        pass

    @Rule(AND(DinnerEastren_Food(chickpeas=True), DinnerEastren_Food(bread=True)), salience=2)
    def action86(self):
        writeOnFile("فتة حمص")
        print("فتة حمص")
        pass

    @Rule(AND(DinnerEastren_Food(thyme=True), DinnerEastren_Food(flour=True)), salience=2)
    def action87(self):
        writeOnFile("مناقيش الزعتر")
        print("مناقيش الزعتر")
        pass

    @Rule(DinnerEastren_Food(chickpeas=True), salience=1)
    def action88(self):
        writeOnFile("فلافل")
        print("فلافل")
        pass

    @Rule(DinnerEastren_Food(cannedmeat=True), salience=1)
    def action89(self):
        writeOnFile("مرتديلا")
        print("مرتديلا")
        pass

    @Rule(DinnerEastren_Food(eggplant=True), salience=1)
    def action90(self):
        writeOnFile("باذنجان مقلي")
        print("باذنجان مقلي")
        pass

    pass


# ke = ChooseEastren_Food()
# ke.reset()
# f = Fact(start="yes")
# ke.declare(f)
# ke.run()
