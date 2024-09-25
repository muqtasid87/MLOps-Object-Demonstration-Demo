from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "Server is running!"


@app.route("/webhook", methods = ["POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        print(f"Webhook received: {data}")
        return jsonify({'status': 'success', 'message':'Webhook received'}), 200
    else:
        return jsonify({'error':'Invalid request method'}), 400
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)