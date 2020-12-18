import pyjokes
import io
from translate import Translator

try:

    translator = Translator(to_lang="ja")
    file = open('./input/input.txt','r')
    content = file.read()
    converted = translator.translate(content)

    with io.open ('./translated file/converted.txt',"w",encoding="utf-8") as my_file:
        my_file.write(converted)



except FileNotFoundError as err:

    print("Please check the path of your input file")
    print("Here's a joke for you")
    print(pyjokes.get_joke('en', 'neutral'))