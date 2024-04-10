import psycopg2
from flask import Flask, render_template
from database_access import *

# con = psycopg2.connect(
#         database="example",
#         user="postgres",
#         password="3005",
#         host="localhost",
#         port='5432'
#     )

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.routes('/new_member_register')
def new_member():
    return

@app.routes('/member_login')
def member_login():
    return

@app.routes('/member_profile')
def member_profile():
    return



if __name__ == '__main__':
    app.run(debug=True)
