# from IPython.core.display import Image, display
# display(Image('nn.png'))

# Used in Tensorflow Model
import numpy as np
import tensorflow as tf

import random
import tflearn

import json
import pickle

from main import *

print("Processing the Intents.....")

with open('intents.json', encoding='utf-8') as json_data:
    intents = json.load(json_data)

import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

nltk.download('punkt')

words = []
classes = []
documents = []
ignore_words = ['!', '?', ',', '.', '-', '_', ' ', '/']
print("Looping through the Intents to Convert them to words, classes, documents and ignore_words.......")
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print("Stemming, Lowering and Removing Duplicates.......")
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

print("Stemming, Lowering and Removing Duplicates.......")
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique stemmed words", words)

print("Creating the Data for our Model.....")
training = []
output = []
print("Creating an List (Empty) for Output.....")
output_empty = [0] * len(classes)

print("Creating Traning Set, Bag of Words for our Model....")
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

print("Shuffling Randomly and Converting into Numpy Array for Faster Processing......")
random.shuffle(training)
training = np.array(training)

print("Creating Train and Test Lists.....")
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Building Neural Network for Out Chatbot to be Contextual....")
print("Resetting graph data....")

tf.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)
print("Training....")

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

# print("Training the Model.......")
# model.fit(train_x, train_y, n_epoch=2000, batch_size=8, show_metric=True)
# model.fit(train_x, train_y, n_epoch=2000, batch_size=8, show_metric=True)

# print("Saving the Model.......")
# model.save('model.tflearn1')
#
# print("Pickle is also Saved..........")
# pickle.dump({'words': words, 'classes': classes, 'train_x': train_x, 'train_y': train_y}, open("training_data", "wb"))

print("Loading Pickle.....")
data = pickle.load(open("training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

with open('intents.json', encoding='utf-8') as json_data:
    intents = json.load(json_data)

print("Loading the Model......")
# load our saved model
model.load('./model.tflearn1')


def clean_up_sentence(sentence):
    # It Tokenize or Break it into the constituents parts of Sentense.
    sentence_words = nltk.word_tokenize(sentence)
    # Stemming means to find the root of the word.
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


# Return the Array of Bag of Words: True or False and 0 or 1 for each word of bag that exists in the Sentence
def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


ERROR_THRESHOLD = 0.25
print("ERROR_THRESHOLD = 0.25")


def classify(sentence):
    # Prediction or To Get the Posibility or Probability from the Model
    results = model.predict([bow(sentence, words)])[0]
    # Exclude those results which are Below Threshold
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # Sorting is Done because heigher Confidence Answer comes first.
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))  # Tuppl -> Intent and Probability
    return return_list


def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # That Means if Classification is Done then Find the Matching Tag.
    if results:
        # Long Loop to get the Result.
        while results:
            for i in intents['intents']:
                # Tag Finding
                if i['tag'] == results[0][0]:
                    # Random Response from High Order Probabilities
                    return random.choice(i['responses'])

            results.pop(0)


def classifyexpert(sentence):
    # Prediction or To Get the Posibility or Probability from the Model
    results = model.predict([bow(sentence, words)])[0]
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append(classes[r[0]])  # Tuppl -> Intent and Probability
    return classes[r[0]]


BYE_INPUTS = ("باي", "إلى اللقاء", "سلام", "وداعاً", "الوداع", "وداعا")
BYE_RESPONSES = ["إلى اللقاء.... أتمنى عودتك قريباً", "وداعاً...أتمنى لك يوم جميل"]


def BYE(sentence):
    for word in sentence.split():
        if word.lower() in BYE_INPUTS:
            return random.choice(BYE_RESPONSES)


thanks_INPUTS = ("عراسي", "شكراً", "ميرسي", "تشكرات", "كفو", "شكرا")
thanks_RESPONSES = ["لا شكر ع واجب ", "تذكر أنني  دائماً موجود  للمساعدة ", "على الرحب والسعة "]


def thanks(sentence):
    for word in sentence.split():
        if word.lower() in thanks_INPUTS:
            return random.choice(thanks_RESPONSES)


recommend_INPUTS = ("جعت", "بتنصحنا", "نصيحة", "اقترح", "يلا لنبلش بالاقتراح", "أكل", "جوعان", "اكل", "اقتراح")
recommend_RESPONSES = [
    "اذا كنت جاهز لعملية اقتراح الأطعمة أدخل نوع الوجبة (فطور - غداء - عشاء ) ... *_* تأكد سوف أبهرك"]


def recommend(sentence):
    for word in sentence.split():
        if word.lower() in recommend_INPUTS:
            return random.choice(recommend_RESPONSES)


help_INPUTS = (
    "ماذا تقدم", "عملك", "شغلك", "شغلتك", "فائدتك", "كيف تستطيع المساعدة", "مساعدة", "ساعدني", "اسمك", "عملك", "عمرك")
help_RESPONSES = ["أهلا بك*_* أنا ربوت الدردشة الذكي أقدم المساعدة من خلال اقتراح الأطعمة المناسبة للمستخدم   "]


def helpp(sentence):
    for word in sentence.split():
        if word.lower() in help_INPUTS:
            return random.choice(help_RESPONSES)


greeting_INPUTS = ("نهار سعيد", "يوم جميل", "هاي", "كيفك", "مرحبا", "هل يوجد أحد هنا ؟", "أستاذ شات", "تحياتي")
greeting_RESPONSES = ["أهللاً بك ....كيف أستطيع مساعدتك ؟"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_INPUTS:
            return random.choice(greeting_RESPONSES)


misunderstand_INPUTS = ("غبي", "مو هيك", "ماعم تفهم", "شبك", "شو صرلك")
misunderstand_RESPONSES = ["*-* لاتيأس إنني أحاول  معرفة ماتريد "]


def misunderstand(sentence):
    for word in sentence.split():
        if word.lower() in misunderstand_INPUTS:
            return random.choice(misunderstand_RESPONSES)


typeNum = 0
mealbreakfast_INPUTS = ("بدي افطر", "ترويقة ", "فطور", "الفطور")
mealbreakfast_RESPONSES = [
    "  تريد وجبة الفطور.(انتبه ! يجب أن تكون مليئة بالعناصر الغذائية). أدخل العناصر المتوفرة لديك وعند الانتهاء اكتب تم    "]


def mealbreakfast(sentence):
    das = 1
    for word in sentence.split():
        if word.lower() in mealbreakfast_INPUTS:
            return random.choice(mealbreakfast_RESPONSES)


meallunch_INPUTS = ("اتغدى", "غداء", "غدا", "الغداء", "الغدا")
meallunch_RESPONSES = [
    "  تريد وجبة الغداء.(انتبه ! يجب أن لا تكون الوجبة دسمة). أدخل العناصر المتوفرة لديك وعند الانتهاء اكتب تم    "]


def meallunch(sentence):
    for word in sentence.split():
        if word.lower() in meallunch_INPUTS:
            return random.choice(meallunch_RESPONSES)


mealdinner_INPUTS = ("اتعشى", "عشا", "عشاء", "العشاء", "العشا")
mealdinner_RESPONSES = [
    "  تريد وجبة العشاء.(انتبه ! يجب أن  تكون الوجبة بسيطة وخفيفة ). أدخل العناصر المتوفرة لديك وعند الانتهاء اكتب تم    "]


def mealdinner(sentence):
    for word in sentence.split():
        if word.lower() in mealdinner_INPUTS:
            return random.choice(mealdinner_RESPONSES)


end_INPUTS = ("تم", "انتهى", "انتهيت", "خلصت")
end_RESPONSES = [" ....تم الانتهاء من عملية الإدخال ...يتم الأن معالجة عمليات الاقتراح"]


def end(sentence):
    for word in sentence.split():
        if word.lower() in end_INPUTS:
            return random.choice(end_RESPONSES)


person_INPUTS = ("اشخاص", "صغير", "كبير", "صغار", "أفراد", "عدد الأشخاص", "أشخاص", "شخص", "كبار", "افراد", "طفل")
person_RESPONSES = [" يتم الأن معالجة عدد الأشخاص"]


def person(sentence):
    for word in sentence.split():
        if word.lower() in person_INPUTS:
            return random.choice(person_RESPONSES)


# Breakfast
elementBreakfast = {

    "foul": False,
    "tomatojam": False,
    "tomato": False,
    "onion": False,
    "flour": False,
    "pasta": False,
    "potato": False,
    "chickpeas": False,
    "cheese": False,
    "strawberry jam": False,
    "oil": False,
    "tomato jam": False,
    "bread": False,
    "goth": False,
    "olive": False,
    "eggs": False,
    "black chocolate": False,
    "white chocolate": False,
    "apricot jam": False,
    "figs jam": False,
    "grape jam": False,
    "corne flakes": False,
    "milk": False,
    "toast": False,
    "honey": False,
    "indomie": False,
    "eggplant": False,
    "rosary": False,
    "tahina": False,
    "yogurt": False,
    "white cheese": False,
    "yellow cheese": False,
    "thyme": False,
    "canned meat": False,
}


def resultBreakfast(listfood):
    print("breakfast")
    for word in elementBreakfast:
        if (word in listfood):
            elementBreakfast[word] = True
            print("ROBO: " + word)
    # print(elementBreakfast )


# Drinks
elementDrinks = {

    "cacao": False,
    "coffee": False,
    "milk": False,
    "nescafe": False,
    "lemon": False,
    "mint": False,
    "apple": False,
    "banana": False,
    "orange": False,
    "honey": False,
    "strawberry": False,
    "mango": False,
    "avocado": False,
    "melon": False,
    "carrots": False,
    "cranberry": False,
    "watermelon": False,
    "kiwi": False,
    "pineapple": False,
    "tea": False,
    "oats": False,
    "cream": False
}


def resultDrinks(listfood):
    print("Drinks")
    for word in elementDrinks:
        if (word in listfood):
            elementDrinks[word] = True
            print("ROBO: " + word)
    # print(elementDrinks)


elementAppetizer = {
    "watercrees": False,
    "sumac": False,
    "gourd": False,
    "eggs": False,
    "tomato": False,
    "shrimp": False,
    "cuokumbber": False,
    "spinach": False,
    "watermelon": False,
    "cheese": False,
    "potato": False,
    "parsley": False,
    "yogurt": False,
    "corn": False,
    "venus": False,
    "mashroom": False,
    "chicken": False,
    "ozyychip": False,
    "eggplant": False,
    "tahina": False,
    "cauliflower": False,
    "garlic": False,
    "chickpeas": False,
    "meat": False,
    "lemon": False,
    "flour": False,
    "beard": False,
    "beans": False,
    "redpepper": False,
    "beet": False,
    "walnut": False,
    "magi": False,
    "lentil": False,
    "grapeleaves": False,
}


def resultAppetizer(listfood):
    print("Appetizer")
    for word in elementAppetizer:
        if (word in listfood):
            elementAppetizer[word] = True
            print("ROBO: " + word)
    # print(elementAppetizer)


elementSweets = {
    "carrots": False,
    "flour": False,
    "apricot": False,
    "lemon": False,
    "butter": False,
    "chocolate": False,
    "cacao": False,
    "egg": False,
    "oil": False,
    "kunafa": False,
    "ghee": False,
    "cream": False,
    "mango": False,
    "strawberry": False,
    "blueberry": False,
    "pineapple": False,
    "creamCheese": False,
    "semolina": False,
    "milk": False,
    "coffee": False,
    "yogurt": False,
    "apple": False,
    "orange": False
}


def resultSweets(listfood):
    print("Sweets")
    for word in elementSweets:
        if (word in listfood):
            elementSweets[word] = True
            print("ROBO: " + word)
    # print(elementSweets)


elementLunch = {
    "rice": False,
    "meat": False,
    "chicken": False,
    "burger": False,
    "peas": False,
    "beans": False,
    "yogurt": False,
    "fish": False,
    "tomato": False,
    "eggplant": False,
    "onion": False,
    "flour": False,
    "flifla": False,
    "pasta": False,
    "potato": False,
    "chickpeas": False,
    "cheese": False,
    "cools": False,
    "mulukhiyah": False,
    "oil": False,
    "goth": False,
    "grape leaves": False,
    "plugs": False,
    "kosa": False,
    "long yellow rice": False,
    "chicken cutlets": False,
    "bamia": False,
    "tomato jam": False,
}


def resultLunch(listfood):
    print("Lunch")
    for word in elementLunch:
        if (word in listfood):
            elementLunch[word] = True
            print("ROBO: " + word)
    # print(elementLunch)


elementDinner = {
    "foul": False,
    "tomatojam": False,
    "tomato": False,
    "onion": False,
    "flour": False,
    "pasta": False,
    "potato": False,
    "chickpeas": False,
    "cheese": False,
    "strawberry jam": False,
    "oil": False,
    "tomato jam": False,
    "bread": False,
    "goth": False,
    "olive": False,
    "eggs": False,
    "black chocolate": False,
    "white chocolate": False,
    "apricot jam": False,
    "figs jam": False,
    "grape jam": False,
    "corne flakes": False,
    "milk": False,
    "toast": False,
    "honey": False,
    "indomie": False,
    "eggplant": False,
    "rosary": False,
    "tahina": False,
    "yogurt": False,
    "white cheese": False,
    "yellow cheese": False,
    "thyme": False,
    "canned meat": False,
}


def resultDinner(listfood):
    print("Dinner : ")
    for word in elementDinner:
        if (word in listfood):
            elementDinner[word] = True
            print("ROBO: " + word)
    # print(elementDinner)


def resultExpertSystem(listfood, typeNum):
    deleteAllFile()
    if os.path.exists("Data Files/result.txt"):
        os.remove("Data Files/result.txt")
        # print("done")
    else:
        print("The file does not exist")

    resultDrinks(listfood)
    resultBreakfast(listfood)
    resultAppetizer(listfood)
    resultLunch(listfood)
    resultSweets(listfood)
    resultDinner(listfood)

    # for word in elementDrinks:
    #     if(word in listfood):
    #         elementDinner[word] = True
    #         print("ROBO: "+ word)

    if (typeNum == 1):
        detectionFoodTable(typeNum, elementSweets, elementBreakfast, elementDrinks, elementAppetizer)
        pass
    elif (typeNum == 3):
        detectionFoodTable(typeNum, elementSweets, elementDinner, elementDrinks, elementAppetizer)
        pass
    elif (typeNum == 2):
        detectionFoodTable(typeNum, elementSweets, elementLunch, elementDrinks, elementAppetizer)
        pass
    else:
        detectionFoodTable(typeNum, elementSweets, elementDinner, elementDrinks, elementAppetizer)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + str(listfood))
        pass
    readfile = open("Data Files/result.txt", "r", encoding="utf-8")
    resultFood = readfile.readline().replace('\n', '')
    readfile.close()
    print("dddddddddddddddddddddddddddddddddddddddddddd\n" + resultFood)
    return resultFood


flag = True
# ["باي" , "إلى اللقاء" , "سلام" , "وداعاً" , "الوداع"],

print("ROBO: " + "أهلا بك*_* أنا ربوت الدردشة الذكي أقدم المساعدة من خلال اقتراح الأطعمة المناسبة للمستخدم   ")


def getMessage(message):
    totalResult = ""
    totalFood = {}
    isEnd = False
    listfood = [" "]
    foodTime = 0
    das = 0
    num = 0
    x = False
    # user_response = input("You- ")
    user_response = message
    user_response = user_response.lower()
    if (BYE(user_response) == None):
        if (greeting(user_response) != None):
            print("ROBO: " + greeting(user_response))
            totalResult = greeting(user_response)
        else:
            if (thanks(user_response) != None):
                print("ROBO: " + thanks(user_response))
                totalResult = thanks(user_response)

            if (recommend(user_response) != None):
                print("ROBO: " + recommend(user_response))
                totalResult = recommend(user_response)

            if (helpp(user_response) != None):
                print("ROBO: " + helpp(user_response))
                totalResult = helpp(user_response)

            if (mealbreakfast(user_response) != None):
                file = open("Data Files/TimeOutput.txt", "a", encoding="utf-8")
                file.write(str(1) + '\n')
                das = 1
                foodTime = 1
                print("ROBO: " + mealbreakfast(user_response))
                totalResult = mealbreakfast(user_response)

            if (meallunch(user_response) != None):
                das = 3
                foodTime = 2
                file = open("Data Files/TimeOutput.txt", "a", encoding="utf-8")
                file.write(str(2) + '\n')
                print("ROBO: " + meallunch(user_response))
                totalResult = meallunch(user_response)

            for word in user_response.split():
                if (word not in ignore_words):
                    if (word not in listfood):
                        listfood.append(classifyexpert(word))
                        file = open("Data Files/FoodOutput.txt", "a", encoding="utf-8")
                        file.write(classifyexpert(word) + '\n')
                        file = open("Data Files/ResOutput.txt", "a", encoding="utf-8")
                        file.write(response(word) + '\n')
                        # print("ROBO: "+ response(word))
            # print("123")

            if (mealdinner(user_response) != None):
                das = 2
                foodTime = 3
                file = open("Data Files/TimeOutput.txt", "a", encoding="utf-8")
                file.write(str(3) + '\n')
                print("ROBO: " + mealdinner(user_response))
                totalResult = mealdinner(user_response)

            if (misunderstand(user_response) != None):
                print("ROBO: " + misunderstand(user_response))
                totalResult = misunderstand(user_response)

            if (end(user_response) != None):
                das = 4
                # لازم يتم استدعاء النظام الخبير أنا عبيت المصفوفات بس مررين وجيبي نتيجة
                foodTime = 0
                if os.path.exists("Data Files/TimeOutput.txt"):
                    readfile = open("Data Files/TimeOutput.txt", "r", encoding="utf-8")
                    foodTime = int(readfile.readline().replace('\n', ''))
                    readfile.close()
                listfood = []
                if os.path.exists("Data Files/FoodOutput.txt"):
                    readfile = open("Data Files/FoodOutput.txt", "r", encoding="utf-8")
                    for line in readfile:
                        line.replace('\n', '')
                        listfood.append(line.replace('\n', ''))
                    readfile.close()
                listRes = []
                ls = []
                if os.path.exists("Data Files/ResOutput.txt"):
                    readfile = open("Data Files/ResOutput.txt", "r", encoding="utf-8")
                    for line in readfile:
                        line.replace('\n', '')
                        ls.append(line.replace('\n', ''))
                    readfile.close()
                    for i in ls:
                        if i not in listRes:
                            listRes.append(i)
                m = "المكونات التي لديك هي :\n"
                for word in listRes:
                    m += word + " - "
                    pass
                m += "\n ونتيج الاقتراح هي :"
                totalResult = m
                totalFood = resultExpertSystem(listfood, foodTime)
                isEnd = True
                print(listfood)
                print("ROBO: " + resultExpertSystem(listfood, foodTime))
                print("ROBO: " + "يمكنك إدخال عدد الأشخاص لمعرفة الكمية المناسبة من الطعام ")
                das = 0
                print("ROBO: " + end(user_response))

            if (person(user_response) != None):
                num = 0
                totalResult = person(user_response)
                print("ROBO: " + person(user_response))
                for word in user_response.split():
                    if (word.isnumeric()):
                        num += int(word)
                print(num)

    else:
        print(BYE(user_response))
        totalResult = BYE(user_response)
        print(listfood)
        flag = False

    return {
        "response" : totalResult ,
        "food" : totalFood,
        "end" : isEnd
    }

# getMessage("غداء")
# getMessage("رز بزاليا سمك ملوخية دجاج فريز مانجا افوكادو برتقال ليمون جزر قهوة كاكاو طحين زيت زبدة سمنة خيار لحمة دجاج ماجي")
# getMessage("تم")
