from passlib.handlers.sha2_crypt import sha256_crypt

from frontend_model.profileModel import *
from flask import session

def getUser():
    return getUserModel()

def getAddress(customer):
    return getAddressModel(customer)

def editnumbercontroller(number):
    return editnumbermodel(number)

def addaddresscontroller(aline1, aline2, state, zipcode, city):
    return addaddressmodel(aline1, aline2, state, zipcode, city)


def editaddresscontroller(aline1, aline2, state, zipcode, city, a_id):
    return editaddressmodel(aline1, aline2, state, zipcode, city, a_id)

def getpaymentcontroller():
    return getpaymentmodel(session['customer'])


def editpaymentcontroller(name, c_type, number, exp_date):
    return editpaymentmodel(name, c_type, number, exp_date)


def editprofilecontroller(fname, lname, email):
    return editprofilemodel(fname, lname, email)


def changePass():
    user = []
    # Connect to MySQL database server using credentials provided
    conn = pymysql.connect(host='localhost',
                                          db='dragonfly_drones', port=3306, user='root', password='')

    cur = conn.cursor()
    # Select the specific customer whose password you want to hash
    cur.execute("SELECT * from customer WHERE c_email = 'javier@gmail.com' ")
    userFound = cur.fetchall()

    # This part isn't necessary here but is shown so student can visualize the DB structure
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "address_line1": users[3],
                    "address_line2": users[4], "city": users[5], "state": users[6], "zipcode": users[7],
                    "email": users[8], "password": users[9], "phone_number": users[10], "card_name": users[11],
                    "card_number": users[12], "exp_date": users[13], "card_type": users[14]})
        # Save the user's password in 'passw'
        passw = users[9]

    # Encrypt the password using the sha256_crypt function
    hash = sha256_crypt.encrypt(passw)

    try:
        # Once encrypted, save this new hashed password to DB
        cur.execute("UPDATE customer SET c_password = %s WHERE c_email = 'javier@gmail.com' ", hash)
        conn.commit()
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


