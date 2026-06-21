# AI Chatbot 

A command-line AI chatbot built using Python and the Google Gemini API.

## Features

* Interactive chatbot conversation
* Google Gemini 2.5 Flash integration
* Environment variable support using `.env`
* Chat history logging
* Exception handling
* Empty input validation
* Exit command support

## Technologies Used

* Python
* Google Gemini API
* python-dotenv
* Git
* GitHub

## Installation

Install the required packages:

```bash
pip install google-generativeai
pip install python-dotenv
```

## Setup

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

## Run the Chatbot

```bash
python chatbot.py
```

## Example

```text
GEMINI CHATBOT
Type 'exit' to end the conversation.

You: What is Python?
Chatbot: Python is a high-level programming language...

You: exit
Exiting the chatbot. Goodbye!
```

## Project Structure

```text
ai-chatbot/
│
├── chatbot.py
├── README.md
├── .gitignore
└── .env
```
