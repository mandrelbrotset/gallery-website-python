#import required modules
from flask import Flask, render_template, request, redirect, flash, url_for
from database import *
import datetime

app = Flask(__name__)

# define urls for pages
not_found = 'no_result.html'
upload = 'upload_image.html'
search_result = 'search_result.html'
error_404 = "404.html"
error_405 = "405.html"
bootstrap = "bootstrap.html"
about = "about.html"
random = "random_image.html"

# homepage
@app.route('/', methods=["GET", "POST"])
def homepage():
	pics = all()
	if request.method == "POST":
		search = request.form['search']
		results = query(search)
		if results != "":
			return render_template(search_result, rows=results)
		elif results == []:
			return render_template(not_found)
	return render_template(bootstrap, rows=pics)

# searchResults page
@app.route('/no_result_found')
def no_result():
	return render_template(not_found)

# search result
#@app.route('/search_result', methods=["GET", "POST"])
#def result(data):
#	return render_template(search_result, rows=data)

# to handle random images page
@app.route('/random_image')
def random_image():
	return render_template(random)

# to handle upload image page
@app.route('/upload_image', methods=["GET", "POST"])
def upload_image():
	if request.method == "POST":
		filename = request.form['file']
	return render_template(upload)

# to handle about page
@app.route('/about')
def about():
	return render_template(about)

# handle errors
@app.errorhandler(404)
def page_not_found(url):
	return render_template(error_404)

@app.errorhandler(405)
def method_not_found(url):
	return render_template(error_405)
# all done



# start app!
if __name__ == '__main__':
	app.run(debug=True)