from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/page1')
def page1():
    return '<h1>Page 1</h1>'

@app.route('/page2')
def page2():
    return '<h1>Page 2</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
