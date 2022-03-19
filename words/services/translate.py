import requests , json
from django.conf import settings

def translate(word):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"
    cleaned_word = word.word if "*" not in word.word else word.word[:-1]
    querystring_word = {"langpair":"en|ne","q":cleaned_word,"mt":"1","onlyprivate":"0","de":"a@b.c"}
    querystring_meaning = {"langpair":"en|ne","q":word.meaning,"mt":"1","onlyprivate":"0","de":"a@b.c"}
    headers = {
        'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
        'x-rapidapi-key': settings.MYMEMORY_TRANSLATE_XRAPID_API_KEY
        }
    try:
        # word and meaning need to be sent separately because the api couldn't translate some words properly when sent combined with their meaning
        response_word = requests.get( url, headers=headers, params=querystring_word)
        response_meaning = requests.get( url, headers=headers, params=querystring_meaning)
        try:
            word_translation = response_word.json()['responseData']['translatedText'] if response_word.json()['responseStatus'] == 200 else ""
            meaning_translation = response_meaning.json()['responseData']['translatedText'] if response_meaning.json()['responseStatus'] == 200 else ""
            if (word_translation == word.word):
                raise Exception
            word.word_translation = word_translation
            word.meaning_translation = meaning_translation
        except Exception as e:
            print(e)
            print("Error in response from MyMachine API. Trying from Microsoft translation API")
            
            url = "https://microsoft-translator-text.p.rapidapi.com/translate"

            querystring = {"from": "en","to":"ne","api-version":"3.0","profanityAction":"NoAction","textType":"plain"}
            w = word.word if "*" not in word.word else word.word[:-1]
            payload = [
                {'Text': w},
                {'Text': word.meaning}
            ]
            payload = str(json.dumps(payload))
            headers = {
                'content-type': "application/json",
                'x-rapidapi-host': "microsoft-translator-text.p.rapidapi.com",
                'x-rapidapi-key': settings.MICROSOFT_TRANSLATE_XRAPID_API_KEY
                }
            try:
                response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
                response = json.loads(response.text)

                if 'error' in response:
                    print(f"Error in Response:{response['error']['message']}")
                else:
                    try:
                        word_translation = response[0]['translations'][0]['text']
                        if 'city' in word_translation.lower():
                            word_translation = word_translation[:word_translation.lower().find('city')]
                        word.word_translation = word_translation
                        word.meaning_translation = response[1]['translations'][0]['text']
                    except Exception as e:
                        print(f'Unpredictable Error:{e}')
                        print(f'Response is: {response}')
            except Exception as e:
                print("Can't make request to Microsoft translation API")
                print(e)
            
    except Exception as e:
        print("Can't make request to MyMemory API")
        print(e)