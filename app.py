from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is my web app.'
    #return 'Hello, World! Cette ligne fera bug le workflow'

@app.route('/about')
def about():
    return 'This is the about page. Please contact us through mail'

if __name__ == '__main__':
    app.run(debug=True)
