from flask import Flask, request, abort
import json
from config import db
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Warning this disables CORS policy

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

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj
@app.get("/api/products")
def get_products():
    products_db= []
    cursor = db.products.find({})
    for prod in cursor:
        products_db.append(fix_id(prod))
    return json.dumps(products_db)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    # products.append(item)
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

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
    

##########################
#final report
catalog = []

@app.get("/api/catalog")
def get_list_products():
    catalog_db = []
    cursor = db.catalog.find({})
    for prod in cursor:
        catalog_db.append(fix_id(prod))
    return json.dumps(catalog_db)

@app.post("/api/catalog")
def save_list_products():
    item = request.get_json()
    print(item)
    db.catalog.insert_one(item)
    return json.dumps(fix_id(item))

@app.delete("/api/catalog/<string:index>")
def delete_products_catalog(index):
    db.catalog.find_one_and_delete({"_id":ObjectId(index)})
    return json.dumps(index)

@app.get("/api/reports/total")
def get_total_price_products():
    total = 0
    total_products = db.catalog.find({})
    for prod in total_products:
        total += prod["price"]
    return json.dumps(total)

@app.get("/api/products/<string:category>")
def get_category_products(category):
    all_products = db.catalog.find({})
    filtered = []
    for prod in all_products:
        if "category" in prod and prod["category"] == category:
            print(prod)
            filtered.append(fix_id(prod))
    if len(filtered) == 0:
        return json.dumps("category not found")
    return json.dumps(filtered)



#######################################################
###############  COUPONS  #############################
#######################################################

# post /api/cupons
# save coupons into a db.coupons collection

@app.post("/api/coupons")
def post_products_coupons():
    coup = request.get_json()
    print(coup)
    db.coupons.insert_one(coup)
    return json.dumps(fix_id(coup))


@app.get("/api/coupons")
def get_products_coupons():
    coup_db = []
    cursor = db.coupons.find({})
    for cp in cursor:
        coup_db.append(fix_id(cp))
    return json.dumps(coup_db)

@app.delete("/api/coupons/<string:index>")
def del_products_coupons(index):
    db.coupons.find_one_and_delete({"_id":ObjectId(index)})
    return json.dumps(index)

@app.get("/api/coupons/<coupon>")
def validate_coupon(coupon):
    code = db.coupons.find_one({"coupon": coupon})
    if code == None:
        print("Error: invalid coupon")
        return abort(404, "Invalid Code")
    return json.dumps(fix_id(code))


# get /api/coupons
# read all the coupons and return them

# coupon
#  code
#  discount


app.run(debug=True)