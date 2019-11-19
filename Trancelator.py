# Language Translator
from googletrans import Translator

translator = Translator() # Create object of Translator.

lang = ['ar', 'zh-tw', 'zh-cn', 'ko', 'pa', 'fr', 'fa', 'es', 'vi']
#lang = ['fa', 'es', 'vi']

for i in range(10):
    text = input()
    for j in lang:
        translated = translator.translate(text) 
        translated = translator.translate(text, src='en', dest=j)
        print(translated.text)
    print(' ')
