import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from database_access import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to connect to the database
def connect_db():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

@app.route('/')
def home():
    return render_template('home.html')

# Route for member login
@app.route('/member_login', methods=['GET', 'POST'])
def member_login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                # Retrieve member information based on email
                sql = """SELECT * FROM Member WHERE Email = %s"""
                cursor.execute(sql, (email,))
                member_info = cursor.fetchone()

                if member_info and member_info[4] == password:
                    session['member_email'] = email
                    return redirect(url_for('member_dashboard'))
                else:
                    return render_template('member_login.html', error_message='Invalid email or password.')

            except (Exception, psycopg2.Error) as error:
                print("Error while retrieving member information:", error)
            finally:
                if conn:
                    conn.close()

    return render_template('member_login.html')

@app.route('/member_logout')
def member_logout():
    # Clear the session data
    session.pop('member_email', None)
    # Redirect the user to the home page or any other desired page
    return redirect(url_for('home'))

# Route for member dashboard
@app.route('/member_dashboard')
def member_dashboard():
    # Check if member is logged in
    if 'member_email' not in session:
        return redirect(url_for('member_login'))

    # Retrieve member information from the database (you'll need to implement this)
    # Example: member_info = get_member_info(session['email'])
    conn = connect_db()
    try:
        cursor = conn.cursor()
        # Retrieve member information based on email
        sql = """SELECT * FROM Member WHERE Email = %s"""
        cursor.execute(sql, (session['member_email'],))
        member_info = cursor.fetchone()
        print(member_info)
        dashboard = display_member_dashboard(member_info[0])
        print(dashboard)
        metrics = display_health_metrics(member_info[0])
        print(metrics)
        fitness = display_fitness_goals(member_info[0])
        print(fitness)
    except (Exception, psycopg2.Error) as error:
                print("Error while retrieving member information:", error)

    return render_template('member_dashboard.html', member_info=member_info, dashboard=dashboard, metrics=metrics, fitness=fitness)

# Route for member profile page
@app.route('/member_profile')
def member_profile():
    # Check if member is logged in
    if 'member_email' not in session:
        return redirect(url_for('member_login'))

    # Retrieve member information from the database (you'll need to implement this)
    # Example: member_info = get_member_info(session['email'])
    conn = connect_db()
    try:
        cursor = conn.cursor()
        # Retrieve member information based on email
        sql = """SELECT * FROM Member WHERE Email = %s"""
        cursor.execute(sql, (session['member_email'],))
        member_info = cursor.fetchone()
        print(member_info)


    except (Exception, psycopg2.Error) as error:
                print("Error while retrieving member information:", error)

    return render_template('member_profile.html', member_info=member_info)

# Route for updating member profile
@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'email' not in session:
        return redirect(url_for('member_login'))

    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']

        phone = request.form['phone']
        member_id = request.form['member_id']
        password = request.form['password']

        # Update member profile in the database
        try:
            update_member_profile(member_id, first_name, last_name, email, password, address, phone)
            return redirect(url_for('member_profile'))
        except Exception as e:
            # Handle any errors that occur during the update process
            return render_template('error.html', error_message=str(e))

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
