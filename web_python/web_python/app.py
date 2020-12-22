from flask import Flask, render_template, request

# экземпляр класса Flask
app = Flask(__name__)

# декоратор маршрутизации
@app.route('/')
def index_page():
	"""
	Функция логики страницы 'index page'
	"""
	return render_template('index.html')

@app.route('/product', methods=['get', 'post'])
def product_page():
	"""
	Функция логики страницы 'product page'
	"""
	message = ''
	if request.method == 'POST':
		site_name = request.form.get('site')
		password = request.form.get('pwd')

		message = site_name + password


	return render_template('product.html', message=message)

@app.route('/contact')
def contact_page():
	"""
	Функция логики страницы 'contact page'
	"""
	return render_template('contact.html')

# конструкция запуска
if __name__ == "__main__":
	app.run(debug=True)