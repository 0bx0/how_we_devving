from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/config_page')
def config_page():
    return render_template("config.html")

# create a new route for the timer page saved as timer_page.html
@app.route('/timer_page')
def timer_page():
    return render_template("timer_page.html")

if __name__ == '__main__':
    app.run(debug=True)
