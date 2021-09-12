import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
     frenchText = language_translator.translate(
         text=englishText,
         model_id='en-fr').get_result()
     return json.dumps(frenchText, indent=2, ensure_ascii=False)

def frenchToEnglish(frenchText):
     englishText = language_translator.translate(
         text=frenchText,
         model_id='fr-en').get_result()
     return json.dumps(englishText, indent=2, ensure_ascii=False)
