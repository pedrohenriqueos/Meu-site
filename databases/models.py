from django.db import models
import pymysql
import pymysql.cursors
from .conf.settings import HOST_DB,PASSWORD_DB,PORT,DB,USER_DB
connection = pymysql.connect(host=HOST_DB,port=PORT, database=DB, user=USER_DB, password=PASSWORD_DB, cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def SaveData(username,name,email,password,address,city,state,cep,check):
    sql = "INSERT INTO User (username,name,email,password) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,(username,name,email,password))
    connection.commit()
    
    sql = "SELECT id FROM User WHERE email=%s"
    cursor.execute(sql,(email))
    id_user = cursor.fetchone()
    street, number = address.split(",")
    sql = "INSERT INTO Address (street,number,city,state,zip,id_user) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,(street,number,city,state,cep,id_user['id']))
    connection.commit()
    
    sql = "INSERT INTO Data (boxcheck,id_user) VALUES(%s,%s)"
    cursor.execute(sql,(check,id_user['id']))
    connection.commit()
    out = {"id": id_user['id'],'username': username, "name": name, "email": email, "password": password, "address": address, "city": city, "state": state, "cep": cep, "check": check}
    return out

def ResquestData(User_id):
    sql = "SELECT name, email FROM User WHERE id=%s"
    cursor.execute(sql,(User_id))
    out = cursor.fetchone()
    sql = "SELECT street, number, city, state, zip FROM Address WHERE id_user=%s"
    cursor.execute(sql,(User_id))
    out2 = cursor.fetchone()
    sql = "SELECT boxcheck FROM Data WHERE id_user=%s"
    cursor.execute(sql,(User_id))
    out3 = cursor.fetchone()
    output = {"name":out['name'], "email":out['email'], "street":out2['street'], "number":out2['number'], "city":out2['city'], "state":out2['state'], "cep":out2['zip'], "boxcheck":out3['boxcheck'] }
    return output

def RequestAll(users_id):
    sql = "SELECT name, email, street, number, city, state, zip, boxcheck FROM User INNER JOIN Address ON User.id = Address.id_user INNER JOIN Data ON User.id = Data.id_user WHERE id = %s"
    values = []
    for id in users_id:
        cursor.execute(sql,(id))
        out = cursor.fetchone()
        values.append(out)
    return values

def AllData(username,password):
    sql = "SELECT id FROM User WHERE username = %s and password = %s"
    cursor.execute(sql,(username,password))
    out = cursor.fetchall()
    sql = "SELECT name, email, street, number, city, state, zip, boxcheck FROM User INNER JOIN Address ON User.id = Address.id_user INNER JOIN Data ON User.id = Data.id_user WHERE id = %s"
    values = []
    for id in out:
        cursor.execute(sql,(id['id']))
        out = cursor.fetchone()
        values.append(out)
    return values
        
def CheckValid(username,password):
    sql = "SELECT password FROM User WHERE username = %s"
    cursor.execute(sql,(username))
    out = cursor.fetchone()
    if out == None:
        return True
    if out['password'] == password:
        return True
    return False