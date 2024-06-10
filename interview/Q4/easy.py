from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'about page'

@app.route('/contact')
def contact():
    return 'Contact us'

if __name__ == '__main__':
    app.run(debug=True)
