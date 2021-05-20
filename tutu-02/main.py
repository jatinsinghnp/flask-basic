
from flask import Flask,escape

app = Flask('__name__')


@app.route('/')
@app.route('/home')
def home():
    return "hellow khjkkhkjhjkhjhkhj"


@app.route('/login/<int:nik>')
def login(nik):
    return f'input u yrs str name {escape(nik)}'

@app.route('/show/<name>')
def show(name):
    return f'input your name {escape(name)}'

@app.route('/slok/<path:testpath>')
def slok(testpath):
    return f'{escape(testpath)}'

if __name__ == '__main__':
    app.run(debug=True)
