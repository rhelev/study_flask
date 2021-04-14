from flask import Flask, render_template

app = Flask(__name__)

def get_films():
    return [{"id": 1, "year": 2001, "name": "1 Step"}, {"id": 2, "year": 2002, "name": "2 Step"}]

@app.route('/')
@app.route('/hello')
def index():
    return render_template("hello.html")

@app.route('/about')
def about():
    films_list = get_films()
    return render_template("about.html", films = films_list, title="TNT")

@app.route('/<string:name>')
def hello_name(name):
    return f"hello {name}"




if __name__ == '__main__':
    app.run()