"""
This module connects with IBM Watson Language Translator service,
and translates text from english to french, and from french to
english.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def english_to_french(english_text=None):
    """
    This method translates text from english to french
    """
    if english_text:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']

    return "No text was provided"

def french_to_english(french_text=None):
    """
    This method translates text from french to english
    """
    if french_text:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']

    return "No text was provided"
