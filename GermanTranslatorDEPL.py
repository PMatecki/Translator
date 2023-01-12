import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
import sys

text=sys.argv[1]

#'Jahrtausendelang ging man davon aus, dass auch der Sender einen geheimen Schlüssel, und zwar den gleichen wie der Empfänger, benötigt.'

# text='For thousands of years it was assumed that the sender also needed a secret key, the same as the recipient.'

tokens = nltk.word_tokenize(text)
tokens = [tok.lower() for tok in tokens]
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(tok) for tok in tokens]
tokens = [word for (word, pos) in nltk.pos_tag(tokens) if pos[0] == 'N']

# print (tokens)

from HanTa import HanoverTagger as ht
tagger = ht.HanoverTagger('morphmodel_ger.pgz')
words = nltk.word_tokenize(text)


# extract Nouns
tokensNounsOriginal=[word for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'NN']
tokensNounsInfinitiv=[x for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'NN']

# extract Adjectives
tokensAdjOriginal=[word for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'ADJA' or pos == 'ADJD' or pos == 'ADV']
tokensAdjInfinitiv=[x for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'ADJA'or pos == 'ADJD' or pos == 'ADV']

# extract Verbs
tokensVerbOriginal=[word for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'VVFIN' or pos == 'VAFIN' or pos == 'VVPP' or pos == 'VVINF']
tokensVerbInfinitiv=[x for (word,x,pos) in tagger.tag_sent(words,taglevel= 1) if pos == 'VVFIN' or pos == 'VAFIN'or pos == 'VVPP' or pos == 'VVINF']

print(tagger.tag_sent(words))
print(tokensNounsOriginal[0:])
print(tokensNounsInfinitiv[0:])
print(tokensAdjOriginal[0:])
print(tokensAdjInfinitiv[0:])
print(tokensVerbOriginal[0:])
print(tokensVerbInfinitiv[0:])

# abc = ' '.join(tokensNounsOriginal)

# from googletrans import Translator
# source_text = abc
# translator = Translator()
# result = translator.translate(source_text,dest='pl', src='de')
#
# print(result.text)