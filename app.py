from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Dữ liệu nhận được từ Telegram
    print(data)  # In ra dữ liệu để kiểm tra
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
