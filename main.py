#Импорт
from flask import Flask, render_template,request, redirect, url_for
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(300), nullable=False)

with app.app_context():
    db.create_all()

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    button_unity = request.form.get('button_unity')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db, button_unity=button_unity)



@app.route('/feedback', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email= request.form['email']
        text = request.form['text']
        
        #Задание №3. Реализовать запись пользователей
        
        user = User(email=email, text=text)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
