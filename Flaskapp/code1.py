from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='uname', passwd='Celebal@77421', database='test_database')

app = Flask(__name__)

@app.route('/')
def main():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT Pincode,SUM(Population) FROM data1 INNER JOIN dataset0 USING(ID) WHERE Cities = "Jaipur" GROUP By Pincode ')
    data = mycursor.fetchall()
    return str(data)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
