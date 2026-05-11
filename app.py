from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Railway deployed!</h1><p>auto-deploy from github</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
