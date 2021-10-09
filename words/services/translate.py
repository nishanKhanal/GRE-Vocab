import requests , json
from django.conf import settings

def translate(word):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"

    querystring = {"from": "en","to":"ne","api-version":"3.0","profanityAction":"NoAction","textType":"plain"}
    payload = [
        {'Text': word.word},
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
            print()
        else:
            try:
                word.word_translation = response[0]['translations'][0]['text']
                word.meaning_translation = response[1]['translations'][0]['text']
            except Exception as e:
                print(f'Unpredictable Error:{e}')
                print(f'Response is: {response}')
    except Exception as e:
        print("Can't make request")
        print(e)