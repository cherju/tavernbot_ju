def dialog_flow(message, token):
    from apiai import ApiAI     # TODO API переехал на v2, переделать или найти другой источник
    import json
    request = ApiAI(token).text_request()
    request.lang = 'ru'
    request.session_id = 'barmen-gxppsm'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    request = None
    if 'result' in response:
        response = response['result']['fulfillment']['speech']
        if response:
            return response
    else:
        return None


if __name__ == '__main__':
    from settings import CHATBOT_TOKEN
    while True:
        msg = input()
        print(dialog_flow(msg, CHATBOT_TOKEN))

