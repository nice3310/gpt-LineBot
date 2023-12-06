import functions_framework
import requests
import os

API_KEY = os.environ.get('API_KEY')
LINE_ACCESS_TOKEN = os.environ.get('LINE_ACCESS_TOKEN')

conversation_history = {}

@functions_framework.http
def api_connection(request):
    request_data = request.get_json(silent=True)

    if 'events' in request_data:
        line_events = request_data['events']
        if line_events:
            line_event = line_events[0]
            user_message = line_event.get('message', {}).get('text', '')
            reply_token = line_event.get('replyToken')

            previous_conversation = conversation_history.get('history', [])

            previous_conversation.append({"role": "user", "content": user_message})

            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {API_KEY}'
                },
                json={
                    'model': 'gpt-3.5-turbo-1106',
                    'messages': previous_conversation,
                }
            )
            response_j = response.json()
            chatbot_response = response_j['choices'][0]['message']['content']

            previous_conversation.append({"role": "assistant", "content": chatbot_response})

            if len(previous_conversation) > 4096:
                previous_conversation = []

            conversation_history['history'] = previous_conversation

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
            }
            reply_data = {
                "replyToken": reply_token,
                "messages": [{"type": "text", "text": chatbot_response}]
            }
            requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=reply_data)
            print(reply_data)

    return 'OK'
