import pymysql
from frontend_model.connectDB import *

# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences

def getProductsModel():
    productList = []
    db = Dbconnect()
    query = "SELECT * FROM products WHERE p_status = 'active';"
    results = db.select(query)
    for res in results:
        productList.append({"id": res['p_id'], "name": res['p_name'], "brand": res['p_brand'], "desc": res['p_desc'],
                    "wifi": res['p_wifi'], "video_res": res['p_video_res'], "color": res['color'], "img": res['p_img'],
                    "stock": res['stock'], "cost": res['p_cost'], "price": res['p_price'], "status": res['p_status']})
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    db = Dbconnect()
    query = ("SELECT DISTINCT p_brand "
             "FROM products "
             "WHERE p_status = 'active'"
             "ORDER BY p_brand;")
    brands = db.select(query)
    return brands

def getColorsModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT color "
             "FROM products "
             "WHERE p_status = 'active'"
             "ORDER BY color;")
    colors = db.select(query)
    return colors


def getVideoResModel():
    db = Dbconnect()
    query = ("SELECT DISTINCT p_video_res "
             "FROM products "
             "WHERE p_status = 'active';")
    videores = db.select(query)
    return videores


def getWifiModel():
    wifi = ['Yes', 'No']
    return wifi
