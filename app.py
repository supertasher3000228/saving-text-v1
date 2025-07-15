from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # В продакшене используйте более безопасный ключ


@app.route('/', methods=['GET', 'POST'])
def index():
    # Инициализируем список сохраненных текстов в сессии, если его нет
    if 'saved_texts' not in session:
        session['saved_texts'] = []

    if request.method == 'POST':
        # Получаем текст из формы
        user_text = request.form.get('user_input', '').strip()

        # Если текст не пустой, добавляем его к сохраненным текстам
        if user_text:
            session['saved_texts'].append(user_text)
            session.modified = True  # Помечаем сессию как измененную

        # Перенаправляем на ту же страницу (POST-redirect-GET паттерн)
        return redirect(url_for('index'))

    # Для GET запроса отображаем страницу с сохраненными текстами
    return render_template('index.html', saved_texts=session['saved_texts'])


@app.route('/clear')
def clear():
    """Маршрут для очистки всех сохраненных текстов"""
    session['saved_texts'] = []
    session.modified = True
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
