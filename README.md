# Project 1: AI Chatbot with Memory (Google Gemini) — README

This chatbot runs in the terminal, uses **Google Gemini**, and remembers
previous messages during a conversation via an in-memory history array.

---

## 1. Requirements

- **Python 3.9 or higher** installed on your computer.
- Internet connection.
- A **FREE API key** from Google (get it from Google AI Studio — no
  credit card required).

---

## 2. File Structure

After extracting the zip, you will see this folder:

```
project1_chatbot_gemini/
├── chatbot_gemini.py    <- main program
├── requirements.txt     <- dependencies list
├── .env.example         <- sample API key file
└── README.md            <- this guide
```

Place the entire folder anywhere (Desktop/Documents). Just remember the
path — you need to open the terminal in that folder to run it.

---

## 3. Setup — Step by Step

### Step A: Create a FREE Gemini API Key
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with your Google account.
3. Click **"Create API Key"**.
4. Copy the key (it will look like: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX`)

> This is completely FREE — no credit card required.

### Step B: Open Terminal / Command Prompt
- **Windows:** Navigate into the folder, type `cmd` in the address bar, and press Enter.
- **Mac/Linux:** Open Terminal and use `cd` to reach the folder:
  ```
  cd path/to/project1_chatbot_gemini
  ```

### Step C: Install Dependencies
```
pip install -r requirements.txt
```
(If `pip` doesn't work, try `pip3`)

### Step D: Set Up the API Key
1. Rename `.env.example` to `.env`.
2. Open `.env` (with Notepad or any text editor).
3. Replace `your_api_key_here` with your actual key:
   ```
   GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

---

## 4. How to Run the Program

In the same terminal (opened inside the folder), run:

```
python chatbot_gemini.py
```
(If you get an error, try `python3 chatbot_gemini.py`)

---

## 5. How to Provide Input

Once the program starts, you'll see a screen like this:

```
============================================================
  DecodeLabs Project 1 - AI Chatbot with Memory (Gemini)
  Model: gemini-flash-latest
  Type your message and press Enter.
  Type 'exit' or 'quit' to end the session.
============================================================

You:
```

Type your message here, for example:
```
You: Hi, my name is Ali
```
Press Enter, and the AI will reply.

Then type the next message:
```
You: What's my name?
```

---

## 6. Example Output

```
You: My name is Vipin
AI: Nice to meet you, Vipin! How can I help you today?

You: Write a short poem about technology
AI: In circuits deep and wires bright,
    Machines now dance with human light...
    (full poem appears here)

You: What is my name?
AI: Your name is Vipin.

You: exit

Session ended. Goodbye!
```

The third response (`Your name is Vipin`) proves that the chatbot
remembered the name from the history array — this is the core
requirement of the project.

---

## 7. Troubleshooting

| Error | Cause | Solution |
|---|---|---|
| `GEMINI_API_KEY not found` | `.env` file missing or key not set | Re-do Step D |
| `API_KEY_INVALID` | Key copied incorrectly | Re-copy the key from AI Studio |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` again |
| `RESOURCE_EXHAUSTED` | Free tier daily limit reached | Wait a while or try again tomorrow |
| `404 NOT_FOUND ... no longer available` | Google retired the model (common) | In `chatbot_gemini.py`, change `MODEL_NAME` to `"gemini-flash-latest"` or `"gemini-3.5-flash"`. Latest list: https://ai.google.dev/gemini-api/docs/models |
| `python` not recognized in terminal | Python not installed or not in PATH | Try `python3` or install from python.org |

---

## 8. Key Skills This Project Teaches

- API integration with Google's official `google-genai` SDK
- Session / conversation state management
- Gemini role schema: `user` and `model` (not assistant)
- Sliding-window (FIFO) history pruning to avoid token overflow
- Input validation before hitting the API

Happy building! 🚀
