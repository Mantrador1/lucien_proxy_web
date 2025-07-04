from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
LOCAL_LUCIEN_URL = os.environ.get("LUCIEN_LOCAL_URL", "http://localhost:8080/ask")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    try:
        res = requests.post(LOCAL_LUCIEN_URL, headers={"Authorization": f"Bearer {os.environ.get(\"OPENROUTER_API_KEY\", \"\")}"}, json={"prompt": prompt})
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
