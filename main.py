import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
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

'''
@app.routes('/new_member_register')
def new_member():
    return

@app.routes('/member_login')
def member_login():
    return

@app.routes('/member_profile')
def member_profile():
    return'''

# Route for member login
@app.route('/member_login', methods=['GET', 'POST'])
def member_login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']

        info = display_member_dashboard(email)
        if info[4] == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error_message='Invalid email or password.')
        # Validate login credentials (you'll need to implement this)
        # Example: if login_successful(email, password):
        #            session['email'] = email
        #            return redirect(url_for('dashboard'))
        #         else:
        #            return render_template('login.html', error_message='Invalid email or password.')

    return render_template('member_login.html')

# Route for member dashboard
@app.route('/member_dashboard')
def dashboard():
    # Check if member is logged in
    if 'email' not in session:
        return redirect(url_for('member_login'))

    # Retrieve member information from the database (you'll need to implement this)
    # Example: member_info = get_member_info(session['email'])

    return render_template('member_dashboard.html', member_info=member_info)

# Route for member profile page
@app.route('/member_profile')
def profile():
    # Check if member is logged in
    if 'email' not in session:
        return redirect(url_for('member_login'))

    # Retrieve member information from the database (you'll need to implement this)
    # Example: member_info = get_member_info(session['email'])

    return render_template('member_profile.html', member_info=member_info)

# Route for scheduler management booking
# @app.route('/schedule', methods=['GET', 'POST'])
# def schedule_management():
#     # Check if member is logged in
#     if 'email' not in session:
#         return redirect(url_for('member_login'))
#
#     if request.method == 'POST':
#         # Retrieve form data and process scheduling (you'll need to implement this)
#         # Example: schedule_info = request.form
#         #          schedule_session(schedule_info)
#
#     return render_template('schedule.html')



if __name__ == '__main__':
    app.run(debug=True)
