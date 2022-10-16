from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<a href="http://127.0.0.1:4444/goyal">click me</a>
</html>"""

@app.route('/goyal')
def goyal():
    return "Hello Mahak Goyal"

@app.route('////resume')
def resume():
    return "Resume"
app.run(port=4444, debug=True)