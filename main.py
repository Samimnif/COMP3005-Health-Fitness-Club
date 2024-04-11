import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session
from database_access import *
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.template_filter('string_to_time')
def string_to_time(value):
    parts = value.split(':')
    hour = int(parts[0])
    minute = int(parts[1].split()[0])  # Extract minutes and remove AM/PM
    return datetime.time(hour, minute)


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


@app.route('/member_register', methods=['GET', 'POST'])
def member_register():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        phone = request.form['phone']

        # Register the member
        register_member(first_name, last_name, email, password, address, phone)
        return redirect(url_for('member_login'))  # Redirect to login page after registration

    return render_template('member_register.html')


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

    return render_template('member_dashboard.html', member_info=member_info, dashboard=dashboard, metrics=metrics,
                           fitness=fitness, billings=get_member_billing(member_info[0]))


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


@app.route('/add_health_metric', methods=['POST'])
def add_health_metric():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        muscle_mass = request.form['muscle_mass']
        bpm = request.form['bpm']
        data_date = request.form['data_date']
        member_id = request.form['member_id']

        insert_health_metric(member_id, height, weight, muscle_mass, bpm, data_date)
        return redirect(url_for('member_dashboard'))


@app.route('/add_fitness_goal', methods=['POST'])
def add_fitness_goal():
    if request.method == 'POST':
        description = request.form['description']
        goal_weight = request.form['goal_weight']
        goal_time = request.form['goal_time']
        burned_calories = request.form['burned_calories']
        total_sets = request.form['total_sets']
        total_reps = request.form['total_reps']
        member_id = request.form['member_id']

        insert_fitness_goal(member_id, description, goal_weight, goal_time, burned_calories, total_sets, total_reps)
        return redirect(url_for('member_dashboard'))


# Trainer login route
@app.route('/trainer_login', methods=['GET', 'POST'])
def trainer_login():
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
                sql = """SELECT * FROM Trainer WHERE Email = %s"""
                cursor.execute(sql, (email,))
                trainer_info = cursor.fetchone()

                if trainer_info and trainer_info[4] == password:
                    session['trainer_email'] = email
                    return redirect(url_for('trainer_scheduler'))
                else:
                    return render_template('trainer_login.html', error_message='Invalid email or password.')

            except (Exception, psycopg2.Error) as error:
                print("Error while retrieving trainer information:", error)
            finally:
                if conn:
                    conn.close()
    return render_template('trainer_login.html')


# Trainer scheduler management route
@app.route('/trainer_scheduler', methods=['GET', 'POST'])
def trainer_scheduler():
    if 'trainer_email' not in session:
        return redirect(url_for('trainer_login'))
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            # Retrieve member information based on email
            sql = """SELECT * FROM Trainer WHERE Email = %s"""
            cursor.execute(sql, (session['trainer_email'],))
            trainer_info = cursor.fetchone()

        except (Exception, psycopg2.Error) as error:
            print("Error while retrieving trainer information:", error)
        finally:
            if conn:
                conn.close()

    trainer_schedule = get_trainer_availabilities(trainer_info[0])

    # Assuming you have time slots and days of the week defined somewhere in your code
    # Example:
    time_slots = ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
                  '17:00', '18:00', '19:00', '20:00', '21:00']
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    return render_template('trainer_scheduler.html', trainer_info=trainer_info, time_slots=time_slots,
                           days=days_of_week, schedule=trainer_schedule)


@app.route('/update_trainer_schedule', methods=['POST'])
def update_trainer_schedule():
    if 'trainer_email' not in session:
        return redirect(url_for('trainer_login'))

    # Get the trainer's ID from the session
    trainer_email = session['trainer_email']
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            # Retrieve trainer information based on email
            sql = """SELECT TrainerID FROM Trainer WHERE Email = %s"""
            cursor.execute(sql, (trainer_email,))
            trainer_id = cursor.fetchone()[0]

            # Retrieve availabilities from the form data
            availabilities = request.form.getlist('availabilities[]')
            print(availabilities)

            # Update trainer schedule in the database
            set_trainer_availability(trainer_id, availabilities)

            return redirect(url_for('trainer_scheduler'))

        except (Exception, psycopg2.Error) as error:
            print("Error while updating trainer schedule:", error)
        finally:
            if conn:
                conn.close()

    return redirect(url_for('trainer_login'))


# Trainer search route
@app.route('/trainer_search')
def trainer_search():
    # Get the list of members
    members = list_member()  # Assuming list_members() returns the list of members

    return render_template('trainer_search.html', members=members)


@app.route('/trainer_search_result/<int:member_id>')
def trainer_search_result(member_id):
    if 'trainer_email' not in session:
        return redirect(url_for('trainer_login'))
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            # Retrieve member information based on email
            sql = """SELECT * FROM Trainer WHERE Email = %s"""
            cursor.execute(sql, (session['trainer_email'],))
            trainer_id = cursor.fetchone()[0]

        except (Exception, psycopg2.Error) as error:
            print("Error while retrieving trainer information:", error)
        finally:
            if conn:
                conn.close()
    if display_member_dashboard(member_id):
        print(get_schedule(member_id, trainer_id))
        return render_template('trainer_search_result.html', member=display_member_dashboard(member_id),
                               personalSessions=get_schedule(member_id, trainer_id))
    else:
        return "Member not found."
    return redirect(url_for('trainer_login'))


@app.route('/staff_login', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        # Check login credentials
        staff_info = get_staff_info(request.form['username'])
        if request.form['password'] == staff_info[4]:
            session['staff_username'] = request.form['username']
            return redirect(url_for('staff_dashboard'))
        else:
            return render_template('staff_login.html', error_message='Invalid username or password.')
    return render_template('staff_login.html')


@app.route('/staff_dashboard')
def staff_dashboard():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))
    staff_info = get_staff_info(session['staff_username'])
    return render_template('staff_dashboard.html', staff_info=staff_info)


# Add the following route to the Flask app
@app.route('/room_booking')
def room_booking():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))
    # Add your room booking logic here
    return render_template('room_booking.html')


# Add the following route to the Flask app
# @app.route('/equipment_view_maintenance')
# def equipment_view_maintenance():
#     if 'staff_username' not in session:
#         return redirect(url_for('staff_login'))
#     # Add your equipment viewing and maintenance logic here
#     return render_template('equipment_view_maintenance.html', equipment=get_equipments())

@app.route('/update_equipment_maintenance', methods=['POST'])
def update_equipment_maintenancef():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))

    equipment_id = request.form.get('equipment_id')
    last_maintenance_date = request.form.get('last_maintenance_date')
    next_maintenance_date = request.form.get('next_maintenance_date')

    # Update equipment maintenance in the database
    update_equipment_maintenance(equipment_id, last_maintenance_date, next_maintenance_date)

    print('Equipment maintenance updated successfully!', 'success')
    return redirect(url_for('equipment_view_maintenance'))


@app.route('/equipment_view_maintenance', methods=['GET', 'POST'])
def equipment_view_maintenance():
    if request.method == 'POST':
        name = request.form['name']
        last_maintenance_date = request.form['last_maintenance_date']
        next_maintenance_date = request.form['next_maintenance_date']
        add_equipment(name, last_maintenance_date, next_maintenance_date)
        return redirect(url_for('equipment_view_maintenance'))
    else:
        equipment = get_equipments()  # Function to retrieve equipment data from the database
        return render_template('equipment_view_maintenance.html', equipment=get_equipments())


# Add the following route to the Flask app
@app.route('/class_scheduler')
def class_scheduler():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))
    print(get_classes())
    # Add your class scheduling logic here
    return render_template('class_scheduler.html', classes=get_classes(), rooms=get_rooms(), trainers=get_trainers())


@app.route('/add_class', methods=['POST'])
def add_class_route():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))
    if request.method == 'POST':
        class_name = request.form['class_name']
        trainer_id = request.form['trainer_id']
        room_id = request.form['room_id']
        start_time = request.form['start_time']
        duration = request.form['duration']
        day_of_week = request.form['day_of_week']
        add_class(class_name, trainer_id, room_id, start_time, duration, day_of_week)
    return redirect(url_for('class_scheduler'))


@app.route('/delete_class', methods=['POST'])
def delete_classf():
    if 'staff_username' not in session:
        return redirect(url_for('staff_login'))

    class_id = request.form.get('delete_class_id')

    if class_id:
        delete_class(class_id)
        print('Class deleted successfully!', 'success')
    else:
        print('Class ID not provided.', 'error')

    return redirect(url_for('class_scheduler'))


# Route to display billing page
@app.route('/billing', methods=['GET', 'POST'])
def billing():
    if request.method == 'POST':
        member_id = request.form['member_id']
        amount = request.form['amount']
        date = request.form['date']
        description = request.form['description']
        process_payment(member_id, amount, date, description)
        return redirect(url_for('billing'))
    else:
        billings = get_billings()  # Function to retrieve billing data from the database
        return render_template('billing.html', billings=billings)

@app.route('/pay_payment', methods=['POST'])
def process_payment_route():
    if request.method == 'POST':
        # Get the transaction_id from the form data
        transaction_id = request.form.get('transaction_id')
        print("Transaction:", transaction_id)
        if transaction_id is None:
            return "Error: Transaction ID not provided in the request"

        # Get other form data from the form
        member_id = request.form.get('member_id')
        amount = request.form.get('amount')
        date = request.form.get('date')
        description = request.form.get('description')

        # Process payment
        pay_payment(transaction_id)

    return redirect(url_for('member_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
