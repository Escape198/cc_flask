from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    print(url_for('home'))
    return render_template('home.html')

@app.route("/index")
def index():
    print(url_for('index'))
    return render_template('index.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
