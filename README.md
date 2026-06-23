# AI Chatbot

A simple command-line AI chatbot built using Python and the Google Gemini API.

## Features

* Conversational AI using Gemini
* Session memory using chat history
* Timestamped chat logging
* Secure API key management with `.env`
* Error handling for API requests
* Exit command to end the chat

## Setup

Install dependencies:

```bash
pip install google-generativeai python-dotenv
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the chatbot:

```bash
python chatbot.py
```

## Files

* `chatbot.py` – Main chatbot program
* `.env` – Stores API key
* `chat history.txt` – Stores conversations
* `.gitignore` – Prevents sensitive files from being tracked

