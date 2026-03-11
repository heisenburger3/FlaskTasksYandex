from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    return render_template('base.html', title='Заготовка')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/mars')
def mars():
    return 'Миссия Колонизация Марса'


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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" surname="surname">
                                    <input type="name" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="jobSelect">Какие у Вас есть профессии?</label>
                                        <select job="form-control" id="classSelect" name="job">
                                          <option>Инженер-исследователь</option>
                                          <option>Инженер-строитель</option>
                                          <option>Пилот</option>
                                          <option>Метеоролог</option>
                                          <option>Инженер по жизнеобеспечению</option>
                                          <option>Инженер по радиационной защите</option>
                                          <option>Врач</option>
                                          <option>Экзобиолог</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['job'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
