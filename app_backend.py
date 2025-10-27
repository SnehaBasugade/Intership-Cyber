# app_backend.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from predict import predict_url  

app = Flask(__name__)
CORS(app)  

@app.route("/check_url", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    score, prediction = predict_url(url)
    return jsonify({"score": score, "prediction": prediction})



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)