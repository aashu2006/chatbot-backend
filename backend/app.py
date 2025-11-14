from flask import Flask, request, jsonify
from flask_cors import CORS
from google.genai import Client

app = Flask(__name__)
CORS(app)

client = Client(api_key="AIzaSyDhXzj4_YonjqTSdTkbxnbpbEET38N1bSQ")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json["message"]

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",  
            contents=user_msg
        )

        reply = response.candidates[0].content.parts[0].text
        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Server error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
