from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'after-all-this-time?-always'


@app.route("/")
@app.route("/home")
def home():
    print(url_for('home'))
    return render_template('home.html')

@app.route("/index")
def index():
    print(url_for('index'))
    return render_template('index.html')

@app.route("/feedback", methods=['POST', 'GET'])
def feedback():
    print(url_for('feedback'))
    if request.method == 'POST':
        print(request.form)
    return render_template('feedback.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
