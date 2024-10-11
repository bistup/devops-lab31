from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return '<a href="/about">About page</a>'
@app.route('/about')
def about():
    return 'This is the About page.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
