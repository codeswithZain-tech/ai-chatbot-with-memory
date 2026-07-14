# AI Chatbot with Memory

A conversational terminal application powered by **Google Gemini** that remembers previous messages during a live session using an in-memory history array with sliding-window pruning.

Part of **DecodeLabs Generative AI Industrial Training Kit (Batch 2026)**.

---

## Features

- Maintains full conversation history within a session
- Sliding-window (FIFO) pruning to prevent token overflow
- Input validation guard (blocks empty/whitespace messages)
- Proper Gemini role schema (`user` / `model` with `parts` array)
- Error handling for API failures

---

## Requirements

- Python 3.9+
- Internet connection
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) (no credit card required)

---

## Setup

```bash
# Navigate to the project folder
cd p1_AI_Chatbot_with_Memory

# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and paste your Gemini API key:
# GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## Usage

```bash
python chatbot_gemini.py
```

Type your messages normally. Type `exit` or `quit` to end the session.

```
============================================================
  DecodeLabs Project 1 - AI Chatbot with Memory (Gemini)
  Model: gemini-flash-latest
  Type your message and press Enter.
  Type 'exit' or 'quit' to end the session.
============================================================

You: My name is Vipin
AI: Nice to meet you, Vipin! How can I help you today?

You: Write a short poem about technology
AI: In circuits deep and wires bright...

You: What is my name?
AI: Your name is Vipin.

You: exit

Session ended. Goodbye!
```

The third response (`Your name is Vipin`) proves the chatbot retained context from the history array.

---

## Project Structure

```
├── chatbot_gemini.py    Main application
├── requirements.txt     Python dependencies
├── .env.example         API key template
├── .gitignore           Files ignored by git
└── README.md            This guide
```

---

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `GEMINI_API_KEY not found` | `.env` file missing or key not set | Create `.env` from `.env.example` with your key |
| `API_KEY_INVALID` | Key copied incorrectly | Re-copy the key from AI Studio |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `RESOURCE_EXHAUSTED` | Free tier daily limit reached | Wait or upgrade to paid tier |
| `404 NOT_FOUND` | Model has been retired | Update `MODEL_NAME` in `chatbot_gemini.py` — see [model list](https://ai.google.dev/gemini-api/docs/models) |
| `python not recognized` | Python not in PATH | Use `python3` or install from [python.org](https://python.org) |

---

## Skills Covered

- API integration with Google's `google-genai` SDK
- Session state management with in-memory arrays
- Gemini role schema (`user` / `model`)
- Sliding-window (FIFO) history pruning
- Input validation before API transmission

---

## License

This project is part of the DecodeLabs Generative AI Industrial Training Kit.
