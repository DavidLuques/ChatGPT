import openai
import os

#virtual enviroment in windows as O.S.
api_keyGPT = os.environ.get('API_KEY_chatGPT')

if (api_keyGPT):
    openai.api_key =api_keyGPT

    model_engine = "text-davinci-002"
    prompt = "how many planet does it exist ?" #questions should be here...
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)

else:
    print(
        'api-key incorrect or something went wrong!'
    )

