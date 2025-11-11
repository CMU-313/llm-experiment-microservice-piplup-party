import os

from flask import Flask
from flask import request, jsonify
from src.translator import translate_content

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "LLM Experiment Translation Microservice",
        "team": "Piplup Party",
        "endpoints": {
            "/translate": "GET or POST - Translate content"
        },
        "examples": {
            "GET": "/translate?content=hello",
            "POST": 'curl -X POST /translate -H "Content-Type: application/json" -d \'{"content":"your text"}\''
        }
    })

@app.route("/translate", methods=["GET", "POST"])
def translator():
    # Support both GET (query param) and POST (JSON body)
    if request.method == "POST":
        data = request.get_json() or {}
        content = data.get("content", "")
    else:
        content = request.args.get("content", default="", type=str)
    
    try:
        is_english, translated_content = translate_content(content)
        return jsonify({
            "is_english": is_english,
            "translated_content": translated_content,
        })
    except Exception as e:
        # If translation fails for any reason, return safe fallback
        return jsonify({
            "is_english": True,
            "translated_content": content if content else "",
            "error": "Translation service temporarily unavailable"
        }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
