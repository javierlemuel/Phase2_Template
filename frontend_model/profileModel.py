import pymysql
from flask import session
from frontend_model.connectDB import *


def getUserModel():
    user = []
    db = Dbconnect()
    query = "SELECT * from customer WHERE c_id = %s"
    # Find user via the customer ID saved in session
    userFound = db.select(query, session['customer'])

    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users['c_id'], "name": users['c_first_name'], "last_name": users['c_last_name'], "email": users['c_email'],
                     "password": users['c_password'], "phone_number": users['c_phone_number'], "status": users['c_status']})

    # Example: to access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user


def editnumbermodel(number):
    db = Dbconnect()
    query = "UPDATE customer SET c_phone_number = %s WHERE c_id = %s"
    try:
        db.execute(query, (number, session['customer']))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def addaddressmodel(aline1, aline2, state, zipcode, city):
    db = Dbconnect()
    query = ("INSERT INTO ship_address (c_id, address_line_1, address_line_2, city, state, zipcode)"
             " VALUES(%s, %s, %s, %s, %s, %s)")

    db.execute(query, (session['customer'], aline1, aline2, city, state, zipcode))

    return 0

def editaddressmodel(aline1, aline2, state, zipcode, city, a_id):
    db = Dbconnect()
    query = ("UPDATE ship_address SET address_line_1 = %s, address_line_2 = %s, city = %s, "
             "state = %s, zipcode = %s WHERE c_id = %s AND address_id = %s")
    try:
        db.execute(query, (aline1, aline2, city, state, zipcode, session['customer'], a_id))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def getpaymentmodel(customer):
    db = Dbconnect()
    query = "SELECT * FROM payment_method WHERE c_id = %s"

    try:
        methods = db.select(query, (customer,))
        return methods

    except pymysql.Error as error:
        print(error)
        return []


def editpaymentmodel(name, c_type, number, exp_date):
    print("STUDENTS MUST ADD")
    return 0


def editprofilemodel(fname, lname, email):
    db = Dbconnect()
    query = "UPDATE customer SET c_first_name = %s, c_last_name = %s, c_email = %s WHERE c_id = %s"
    try:
        db.execute(query,(fname, lname, email, session['customer']))
        return 0

    except pymysql.Error as error:
        print(error)
        return 1


def getAddressModel(customer):
    db = Dbconnect()
    sql = "SELECT * FROM ship_address WHERE c_id = %s"
    result = db.select(sql, (customer))

    return result

