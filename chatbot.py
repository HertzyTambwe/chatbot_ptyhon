import google.generativeai as ai

API_KEY = 'AIzaSyAOeUMzaSa8YwxWb-D2tRp7D72T4I5I9XQ'

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()

while True:
    message = input('You : ')

    if message.lower() == 'bye':
        print("Chatbot: GoodBye")
        break
    response = chat.send_message(message)
    print('ChatBot: ', response.text)

