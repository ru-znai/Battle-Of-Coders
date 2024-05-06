from flask import Flask, render_template, session, redirect, url_for, request
import files
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
test_cases_even_or_odd = [[[1, 2], 2], [[2, 4], 8], [[-1, 6], -6]]


def get_next_row_from_database(current_id, stat=True):
    if stat:
        conn = sqlite3.connect('base/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, description, function_name, test FROM tasks WHERE id > ? ORDER BY id LIMIT 1',
                       (current_id,))
        row = cursor.fetchone()
        conn.close()
        return row
    else:
        return None


def get_db_connection_lvl():
    conn = sqlite3.connect('base/database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT lvl FROM users WHERE id = ?", (1,))
    current_user_lvl = cursor.fetchone()[0]
    conn.close()
    return current_user_lvl


def write_db_lvl(lvl_new):
    conn = sqlite3.connect('base/database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET lvl =? WHERE id = ?", (lvl_new, 1))
    conn.commit()
    conn.close()


@app.route('/', methods=['POST', 'GET'])
def index():
    result = []
    advice = []
    if request.method == 'POST':
        code_user = request.form['code']
        created_function = files.create_function_from_text(code_user)
        result = files.test_function(created_function, test_cases_even_or_odd)

    current_user_lvl = get_db_connection_lvl()

    if result and False not in result:

        current_user_lvl += 1
        write_db_lvl(current_user_lvl)
    elif result and False in result:

        advice.append(['Не плохо, но еще можно лучше!'])

        advice.append(code_user)

    data = get_next_row_from_database(current_user_lvl)

    return render_template('description.html', data=data, current_user_lvl=current_user_lvl, advice=advice)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Обработка данных из формы
        username = request.form['username']
        password = request.form['password']
        # Дополнительная обработка или проверка данных

        # Вернуть какой-то результат или перенаправление
        return 'Данные получены: {} {}'.format(username, password)

    # Если метод GET, просто отобразить страницу
    return render_template('login.html')

@app.route('/intro', methods=['POST', 'GET'])
def intro():
    return render_template('intro.html')



if __name__ == '__main__':
    app.run(debug=True)
