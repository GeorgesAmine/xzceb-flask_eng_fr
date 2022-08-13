'''
Translator module between english and french
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    This function takes a string in english and translates it to french
    and returns it as a string.
    '''
    if not english_text:
        return 'Cannot translate empty text'

    # The actual call to the translator API, returns a python dictionary
    result = language_translator.translate(text=english_text, model_id='en-fr').get_result()

    # Accessing translations in the response with key: 'translations'
    # This gives a list of all translations
    translations = result['translations']

    # Accessing the actual translation as a string in the first element of translations list
    french_text = translations[0]['translation']

    # Return the translated text
    return french_text

def french_to_english(french_text):
    '''
    This function takes a string in french and translates it to english
    and returns it as a string.
    '''
    if not french_text:
        return 'Cannot translate empty text'

    # The actual call to the translator API, returns a python dictionary
    result = language_translator.translate(text=french_text, model_id='fr-en').get_result()

    # Accessing translations in the response with key: 'translations'
    # This gives a list of all translations
    translations = result['translations']

    # Accessing the actual translation as a string in the first element of translations list
    english_text = translations[0]['translation']

    # Return the translated text
    return english_text
