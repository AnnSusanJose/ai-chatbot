import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    text=input("You: ")
    if text.lower()=="exit":
        print("Exiting the chatbot. Goodbye!")
        break
    res=model.generate_content(text)
    print("Chatbot: ", res.text)