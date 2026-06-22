from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])
print("GEMINI CHATBOT")
print("Type 'exit' to end the conversation.")
while True:
    text=input("You: ")
    if text.lower()=="":
        print("Please enter a message.")
        continue
    if text.strip()=="exit":
        print("Exiting the chatbot. Goodbye!")
        break
    try:
        res=chat.send_message(text)
        print("Chatbot: ", res.text)
        with open("chat history.txt","a") as f:
            f.write("You: "+text+"\n")
            f.write("Chatbot: "+res.text+"\n")
    except Exception as e:
        print("An error occurred:", e)