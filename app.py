from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    print("Received update:", json_data)  # In ra dữ liệu từ Telegram
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
