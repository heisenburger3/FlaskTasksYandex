from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/mars')
def mars():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Реклама</title>
                      </head>
                      <body>
                        <h1>Человечество вырастает из детства.</h1>
                        <h1>Человечеству мала одна планета.</h1>
                        <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                        <h1>И начнем с Марса!</h1>
                        <h1>Присоединяйся!</h1>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
