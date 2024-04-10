import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session

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
                    session['email'] = email
                    return redirect(url_for('member_dashboard'))
                else:
                    return render_template('member_login.html', error_message='Invalid email or password.')

            except (Exception, psycopg2.Error) as error:
                print("Error while retrieving member information:", error)
            finally:
                if conn:
                    conn.close()

    return render_template('member_login.html')

# Route for member dashboard
@app.route('/member_dashboard')
def member_dashboard():
    # Check if member is logged in
    if 'email' not in session:
        return redirect(url_for('member_login'))

    # Retrieve member information from the database (you'll need to implement this)
    # Example: member_info = get_member_info(session['email'])

    return render_template('member_dashboard.html', member_info=member_info)

# Route for member profile page
@app.route('/member_profile')
def member_profile():
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
