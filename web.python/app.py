from flask import Flask, render_template


# экземпляр класса Flask 
app = Flask(__name__)

# декоратор маршрутизации
@app.route('/')
def index_page():
     """
     Функция логики страницы 'index page'

     """
     return render_template('index.html')

# конструкция для запуска
if __name__ == "__main__":
    app.run(debug=True)
