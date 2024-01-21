from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# ランダムなAI応答リスト
responses = [
    "こんにちは！",
    "お元気ですか？",
    "質問があればどうぞ。",
    "ご用があればどうぞお知らせください。"
]

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    # ランダムな応答を選択
    ai_response = random.choice(responses)

    response_data = {
        "user_message": user_message,
        "ai_response": ai_response
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
