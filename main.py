#Импорт
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # Используем SQLite
db = SQLAlchemy(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}>'


with app.app_context():
    db.create_all()


#Запуск страницы с контентом
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('text')

        # Сохраняем комментарий в базу данных
        new_feedback = Feedback(name=name,  comment=comment)
        db.session.add(new_feedback)
        db.session.commit()

        return redirect('/')  # Перенаправляем пользователя обратно на главную страницу

    feedbacks = Feedback.query.all()

    return render_template('index.html', feedbacks=feedbacks)


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)


