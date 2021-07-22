# 1) First we need to install some dependencies
# pip install requests
# pip install playsound
# pip install gtts
# pip install -U PyObjC is needed for sound to work

# 2) Import those functions and libraries
import requests
import ast
from playsound import playsound
from gtts import gTTS

# 3) Get the api https://rapidapi.com/gofitech/api/nlp-translation/
# 4) Paste this url next from the api request
url = "https://nlp-translation.p.rapidapi.com/v1/translate"

# 10) define speech, recieve text and language.
# The language will actually tell gTTS what accent to use
def speech(text, language):
    print(text)
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

# 8) get the users input and convert what they say into what the api needs
translate_from = input("Translate from:\n")
translate_to = input("Translate to:\n")
text = input("Enter your phrase:\n")

if translate_from.lower() == "english":
  translate_from = "en"
elif translate_from.lower() == "spanish" or translate_from.lower() == "espanol":
  translate_from = "es"
elif translate_from.lower() == "french":
  translate_from = "fr"

if translate_to.lower() == "english":
  translate_to = "en"
elif translate_to.lower() == "spanish" or translate_to.lower() == "espanol":
  translate_to = "es"
elif translate_to.lower() == "french":
  translate_to = "fr"

# 4) this goes along with the paste from the api
querystring = {
  "text": text,
  "to": translate_to,
  "from": translate_from
}

headers = {
    'x-rapidapi-key': "7603016162msh8263f88a5aa10dfp18e91ajsna3493aef8fcf",
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# 5) use the ast library to convert the text to a dictionary to query through
dict_response = ast.literal_eval(response.text)
# print(dict_response)

# 6) create a dictionary
translate = {
  "original": text,
  "translated": dict_response["translated_text"]
}

# 7) Store that text value inside of text
text = translate['translated'][translate_to]

# 9) Create a function called speech, put the definition towards the top of the project
# Send it the text, and the converted language
speech(text, translate_to)
