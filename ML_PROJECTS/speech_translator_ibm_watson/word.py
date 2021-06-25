from ibm_watson import SpeechToTextV1, LanguageTranslatorV3

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


"""Authenticator"""
lang_translator_api ="sFtPpFM26XcIzEu7B9fm99f6yppBmFDBrOhI067qnv-3"
lang_translator_url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/10f4a38c-1bbe-484c-935e-6672dd6ab2f9"

speech_to_text_api ="RNv5WMUN2hRAxYNmos23bxwRTwNHYm0w2c7MalVXRhtY"
speech_to_text_url="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/29603c1d-5cf8-4a4c-a2e6-ee35e6b04fc7"

'''lang authenticator'''
#gives back authenticator object
lang_auth = IAMAuthenticator(lang_translator_api)

#language translator object 
lang_translator = LanguageTranslatorV3(version="2018-05-01",authenticator=lang_auth)

lang_translator.set_service_url(lang_translator_url)


'''speech to text authenticator'''
speech_to_text_auth = IAMAuthenticator(speech_to_text_api)
speech_to_text = SpeechToTextV1(authenticator = speech_to_text_auth)

speech_to_text.set_service_url(speech_to_text_url)


"""End Authenticator"""


"""Speech to text"""
with open('hello.mp3','rb') as file:
    result = speech_to_text.recognize(audio=file,content_type='audio/mp3',model='en-AU_NarrowbandModel',continuous=True).get_result()

voice = result['results'][0]['alternatives'][0]['transcript']
print("\n",voice)    
"""End speech to text"""


"""text translate"""
#english to tamil,hindi,telugu
tamil = 'en-ta'
telugu = 'en-te'
hindi = 'en-hi'


translation = lang_translator.translate(text=voice,model_id =hindi).get_result()

translated_text = translation['translations'][0]['translation']

print(translated_text)
"""End text translate"""


print("\nWorking\n")