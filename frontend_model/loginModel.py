from flask import session
from frontend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt

def loginmodel(email, password):

    # Receive email and password to check in the "database"

    user = []
    db = Dbconnect()
    sql = "SELECT c_email, c_id, c_password, c_status FROM customer WHERE c_email = %s"
    # Save user info in list
    userFound = db.select(sql, (email))

    print(userFound)

    for res in userFound:
        user.append({"id": res['c_id'], "email": res['c_email'], "password": res['c_password'], "status": res['c_status']})


    # Save user info in list

    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in user:
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['customer'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"


def registermodel(fname, lname, email, hash):
    # TO BE ADDED BY STUDENTS
    return False
