import os
from ollama import Client

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "mistral:7b")
client = Client(host=OLLAMA_HOST)


def get_translation(post: str) -> str:
    # TODO: Insert context
    # ---------------- YOUR CODE HERE ---------------- #
    context = (
        "You are a language classifier. "
        "If the input text is NOT in English, translate it into English. "
        "If it IS already English, return it unchanged.\n\n"
        "Example:\n"
        "INPUT: ¿Hola, cómo estás?\n"
        "OUTPUT: Hello, how are you?"
    )

    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )

    # Return just the model's output text
    return response.message.content


def get_language(post: str) -> str:
    context = "" # TODO: Insert context
    # ---------------- YOUR CODE HERE ---------------- #
    context = (
        "You are a language classifier. "
        "Identify what language the input text is written in. Reply ONLY with the name of the language."
    )

    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )

    # Return just the model's output text
    return response.message.content


def query_llm(post: str) -> tuple[bool, str]:
  # ----------------- YOUR CODE HERE ------------------ #
  # Step 1: Detect language
  language = get_language(post).strip().lower()

  # If English → return (True, original post)
  if language == "english":
      return (True, post)

  # Otherwise translate
  translation = get_translation(post)
  return (False, translation)


def query_llm_robust(post: str) -> tuple[bool, str]:
  '''
  TODO: Implement this
  '''
  def _to_text(x) -> str:
      """Convert any model output to a string."""
      if x is None:
          return ""
      if isinstance(x, (list, tuple)):
          return " ".join(map(_to_text, x)).strip()
      if isinstance(x, dict):
          for k in ("text", "output", "translation", "message", "content"):
              v = x.get(k)
              if isinstance(v, str):
                  return v.strip()
          return str(x)
      return str(x).strip()

  def _seems_english(sample: str) -> bool:
      """Simple guess: mostly ASCII or says 'english'/'en'."""
      if not sample:
          return True
      ascii_ratio = sum(c.isascii() for c in sample) / max(1, len(sample))
      s = sample.lower()
      return "english" in s or s == "en" or ascii_ratio > 0.92

  # Try to detect language; fall back to a heuristic on failure.
  try:
      lang = _to_text(get_language(post)).lower()
  except Exception:
      lang = ""

  try:
      is_english = (lang == "english") or ("en" in lang and "not" not in lang)
      if not lang:
          is_english = _seems_english(post)
  except Exception:
      is_english = _seems_english(post)

  if is_english:
      text = _to_text(post)
      return True, (text[:4000] if len(text) > 4000 else text)

  # Translate; if anything goes wrong, return a short placeholder.
  try:
      tx = _to_text(get_translation(post))
  except Exception:
      tx = ""
  if not tx:
      tx = "[translation unavailable]"
  return False, (tx[:4000] if len(tx) > 4000 else tx)

