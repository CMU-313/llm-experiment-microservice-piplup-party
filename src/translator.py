from src.llm import query_llm_robust


def translate_content(content: str) -> tuple[bool, str]:
    """
    Translate content using LLM.
    Returns (is_english, translated_content).
    """
    if not content:
        return True, ""
    
    try:
        return query_llm_robust(content)
    except Exception:
        # Fallback if Ollama is offline or any error occurs
        return True, content
