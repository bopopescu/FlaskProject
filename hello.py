import mysql.connector
from flask import Flask, render_template, request

conn = mysql.connector.connect (user = 'admin', password = 'password',
                                host ='127.0.0.1', port='8889', database= 'CSV_DB')
db = conn.cursor()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        zipcode = request.form["zipcode"]
        db.execute("SELECT * FROM TBL_NAME WHERE Zipcode="+ zipcode)

        result = db.fetchall()

       return render_template("index.html", addresses=result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
