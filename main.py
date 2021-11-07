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

m = pymorphy2.MorphAnalyzer()
lem_phrasez = [" ".join([pymorphy2.MorphAnalyzer().parse(word)[0].normal_form for word in text.split()]) for text in texts]
# print(lem_phrasez)
print('\n'.join(lem_phrasez))
