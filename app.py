from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

input_from_python = ["a","b","c"]

@app.route('/')
def index_render():
    return render_template("index.html")

@app.route('/testpage')
def test_page_view():
    return render_template("test_page.html", input_from_python= input_from_python)

@app.route('/test2')
def test2_view():
    return render_template("test2.html", input_from_python= input_from_python)

if __name__ == "__main__":
    app.run(debug=True)