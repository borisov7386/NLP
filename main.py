import pymorphy2
import nltk

# words =['приставки', 'приставкой', 'приставками']
# morph=pymorphy2.MorphAnalyzer()
#
# for word in words:
#     p = morph.parse(word)[0]
#     print(p.normal_form)

texts = ["нихренашеньки ваши роутеры не работает у него", "нихренашеньки ваши роутеры не работает у нас",
         "нихренашеньки ваши роутеры не работает у вас"]
ww= ""

for text in texts:
    p = nltk.word_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()
    for word in p:
        d = morph.parse(word)[0]
        ww = ww + "\n"+ d.normal_form

print(ww)

# text = "нихренашеньки ваши роутеры не работает у него"
#
# p = nltk.word_tokenize(text)
# print(p)
#
# morph=pymorphy2.MorphAnalyzer()
#
# for word in p:
#      d = morph.parse(word)[0]
#      print(d.normal_form)
