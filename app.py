from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# HUGGING FACE CLIENT
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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"
)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# CHAT ROUTE
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    try:

        response = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=300
        )

        ai_reply = response.choices[0].message.content

    except Exception as e:

        ai_reply = str(e)

    return jsonify({
        "reply": ai_reply
    })


# RUN APP
if __name__ == "__main__":
    app.run(debug=True)