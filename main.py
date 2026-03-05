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


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.jpg">
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                        </head>
                        <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="/static/img/mars.jpg">
                            <div class="alert alert-secondary" role="alert">
                             Человечество вырастает из детства.
                              </div>
                                <div class="alert alert-success" role="alert">
                                  Человечеству мала одна планета.
                                    </div>
                                      <div class="alert alert-secondary" role="alert">
                                        Мы сделаем обитаемыми безжизненные пока планеты.
                                          </div>
                                            <div class="alert alert-warning" role="alert">
                                              И начнем с Марса!
                                                </div>
                                                  <div class="alert alert-danger" role="alert">
                                                    Присоединяйся!
                                                      </div>
                            </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
