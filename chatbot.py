import google.generativeai as ai

# Replace with your API key
API_KEY = '"

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

