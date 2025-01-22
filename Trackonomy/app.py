from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return "Welcome to the Personal & Family Finance Tracker!"

if __name__ == '__main__':
    app.run(debug=True)