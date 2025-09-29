from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate-message", methods=["POST"])
def generate_message():
    data = request.json
    prompt = data.get("prompt", "")

    # Predefined templates using name "Jay"
    if "diwali" in prompt.lower():
        message = "Hello Jay, Diwali greetings! We wish you the best holiday. Namaste!"
    elif "new year" in prompt.lower():
        message = "Hello Jay, Wishing you a Happy New Year filled with joy and success!"
    elif "christmas" in prompt.lower():
        message = "Hello Jay, Merry Christmas! May your holidays sparkle with joy."
    else:
        message = f"Hello Jay, here’s a message based on your prompt: {prompt}"

    return jsonify({"generated_message": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
