from googletrans import Translator
import sys

source_text = sys.argv[1]
LangOut = sys.argv[2]
LangIn = sys.argv[3]

translator = Translator()
result = translator.translate(source_text,dest=LangOut, src=LangIn)

print(result.text)