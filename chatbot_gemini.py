"""
Project 1: Custom AI Chatbot with Memory (Google Gemini Version)
DecodeLabs - Generative AI Industrial Training Kit (2026)

GOAL:
Build a conversational terminal that remembers previous messages
during a live session using a stateful, in-memory history array.

KEY REQUIREMENTS COVERED:
1. Connects to a frontier LLM (Google Gemini) using the official
   google-genai SDK + API key.
2. Maintains an active in-memory list to store conversation history.
3. Appends every new user input and model response to the history payload.
4. Input validation guard (blocks empty / whitespace-only messages).
5. Sliding-window (FIFO) pruning so the history never overflows the
   model's context window / token budget.

NOTE: Gemini's official schema uses role "user" and role "model"
(NOT "assistant" like some other providers), and wraps text inside
a "parts" list, e.g. {"role": "user", "parts": [{"text": "hello"}]}
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------
load_dotenv()  # reads variables from a local .env file

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-flash-latest"        # always points to Google's current
                                           # fast frontier model (auto-updates
                                           # when Google releases new versions,
                                           # so this script won't break again)
MAX_HISTORY_MESSAGES = 20                 # sliding window size (FIFO)
SYSTEM_PROMPT = (
    "You are a helpful, friendly AI assistant built for a training "
    "exercise. Keep answers clear and reasonably concise."
)

# ---------------------------------------------------------------------------
# STARTUP CHECKS
# ---------------------------------------------------------------------------
if not API_KEY:
    print("ERROR: GEMINI_API_KEY not found.")
    print("Create a '.env' file (copy .env.example) and paste your key in it.")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

# ---------------------------------------------------------------------------
# STATE: the in-memory conversation history array (H)
# Each entry follows Gemini's required schema:
#   {"role": "user" | "model", "parts": [{"text": "..."}]}
# ---------------------------------------------------------------------------
conversation_history = []


def apply_sliding_window(history: list) -> None:
    """
    FIFO pruning in-place: if the history grows past MAX_HISTORY_MESSAGES,
    drop the oldest messages first while keeping the array valid
    (Gemini's API requires the list to still start with a 'user' turn).
    """
    while len(history) > MAX_HISTORY_MESSAGES:
        history.pop(0)
    if history and history[0]["role"] != "user":
        history.pop(0)


def get_model_response(history: list) -> str:
    """
    Sends the full history array to the GenAI SDK and returns
    the model's text response (R_t).
    """
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        return response.text
    except APIError as e:
        return f"[ERROR] API returned an error: {e}"
    except Exception as e:
        return f"[ERROR] Unexpected error: {e}"


def main():
    print("=" * 60)
    print("  DecodeLabs Project 1 - AI Chatbot with Memory (Gemini)")
    print("  Model:", MODEL_NAME)
    print("  Type your message and press Enter.")
    print("  Type 'exit' or 'quit' to end the session.")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()

        # --- Structural Validation Gate ---
        # Blocks empty / whitespace-only payloads before they reach the API
        if not user_input:
            print("[WARN] Empty message ignored. Please type something.")
            continue

        if user_input.lower() in ("exit", "quit"):
            print("\nSession ended. Goodbye!")
            break

        # --- Step 1: Ingest & Append user input ---
        conversation_history.append(
            {"role": "user", "parts": [{"text": user_input}]}
        )

        # --- Sliding window guard before sending to API ---
        apply_sliding_window(conversation_history)

        # --- Step 2: Transmit full history & get response ---
        print("AI: thinking...", end="\r")
        ai_response = get_model_response(conversation_history)
        print(" " * 20, end="\r")  # clear the "thinking..." line

        # --- Record model response into the same history list ---
        conversation_history.append(
            {"role": "model", "parts": [{"text": ai_response}]}
        )

        # --- Sliding window guard after appending model response too ---
        apply_sliding_window(conversation_history)

        print(f"AI: {ai_response}")


if __name__ == "__main__":
    main()
