from flask import Flask, json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"
# this is just an example
# @app.post("/")
# def homePost():
# return "hello from flask post"

# Endpoints
@app.get("/test")
def test():
    return "hello from the test server"

@app.get("/api/about")
def aboutGet():
    name = {"name" : "Christian"}
    return json.dumps(name)

@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""

# by creating the farewell message

@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:blue>Good bye, {name}!</h1>"""

app.run(debug=True)