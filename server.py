from flask import Flask, request
import json

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

# ################################################
products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    products.append(item)
    return json.dumps(item)

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item = request.get_json()
    if 0<= index <= len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item = request.get_json()
    if 0<= index <=len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "That index does not exist"

# pacth -- the method to update an especific element into python is: .update

@app.patch("/api/products/<int:index>")
def update_specific_element(index):
    update_element = request.get_json()
    if 0<= index <= len(products):
        update_element(index).update(update_element)
        return json.dumps(update_element)
    else:
        return "That index does not exist"

app.run(debug=True)