from flask import Flask, render_template

app = Flask(__name__)

# Flask will automatically call the function declared immediately below the decorator ie index()
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')