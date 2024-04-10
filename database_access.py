import psycopg2
import json

con = psycopg2.connect(
        database="COMP3005GYM",
        user="postgres",
        password="3005",
        host="localhost",
        port='5432'
    )

# Function for Member Registration
def register_member(first_name, last_name, email, password, address, phone):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO Member (FirstName, LastName, Email, Password, Address, Phone)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (first_name, last_name, email, password, address, phone))
        conn.commit()
        print("Member registered successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while registering member:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Getter Function for Member
def list_member():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM Member"""
        cursor.execute(sql)
        members = cursor.fetchall()

        return members
    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving members:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Member Profile Management
def update_member_profile(member_id, first_name, last_name, email, password, address, phone):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """UPDATE Member
                 SET FirstName = %s, LastName = %s, Email = %s, Password = %s, Address = %s, Phone = %s
                 WHERE MemberID = %s"""
        cursor.execute(sql, (first_name, last_name, email, password, address, phone, member_id))
        conn.commit()
        print("Member profile updated successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating member profile:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Member Dashboard Display
def display_member_dashboard(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM Member WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        member_data = cursor.fetchone()
        print("Member Dashboard:")
        print("MemberID:", member_data[0])
        print("Name:", member_data[1], member_data[2])
        print("Email:", member_data[3])
        print("Address:", member_data[5])
        print("Phone:", member_data[6])
        # Add more dashboard display information as needed
        return member_data
    except (Exception, psycopg2.Error) as error:
        print("Error while displaying member dashboard:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for displaying Health Metrics for a Member
def display_health_metrics(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM HealthMetrics WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        health_metrics_data = cursor.fetchall()
        if len(health_metrics_data) == 0:
            print("No health metrics found for the member.")
        else:
            print("Health Metrics for MemberID", member_id)
            for row in health_metrics_data:
                print("HealthMetricID:", row[0])
                print("Height:", row[2])
                print("Weight:", row[3])
                print("MuscleMass:", row[4])
                print("BPM:", row[5])
                print("DataDate:", row[6])
                print("----------------------")

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying health metrics:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for displaying Fitness Goals for a Member
def display_fitness_goals(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM FitnessGoals WHERE MemberID = %s"""
        cursor.execute(sql, (member_id,))
        fitness_goals_data = cursor.fetchall()
        if len(fitness_goals_data) == 0:
            print("No fitness goals found for the member.")
        else:
            print("Fitness Goals for MemberID", member_id)
            for row in fitness_goals_data:
                print("GoalID:", row[0])
                print("Description:", row[2])
                print("Goal Weight:", row[3])
                print("Goal Time:", row[4])
                print("Burned Calories:", row[5])
                print("Total Sets:", row[6])
                print("Total Reps:", row[7])
                print("----------------------")

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying fitness goals:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Member Schedule Management
def schedule_training_session(member_id, trainer_id, start_time, duration):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO PersonalTrainingSession (MemberID, TrainerID, StartTime, Duration)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, trainer_id, start_time, duration))
        conn.commit()
        print("Training session scheduled successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while scheduling training session:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for setting Trainer Availability
def set_trainer_availability(trainer_id, availabilities):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        # Delete existing availability slots for the trainer
        sql_delete = """DELETE FROM TrainerAvailability WHERE TrainerID = %s"""
        cursor.execute(sql_delete, (trainer_id,))
        conn.commit()

        # Insert new availability slots
        for availability in availabilities:
            start_time, end_time, day_of_week = availability
            sql_insert = """INSERT INTO TrainerAvailability (TrainerID, StartTime, EndTime, DayOfWeek)
                            VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql_insert, (trainer_id, start_time, end_time, day_of_week))
            conn.commit()

        print("Trainer availability set successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while setting trainer availability:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Administrative Staff Room Booking Management
def book_room(room_name, capacity):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO Room (RoomName, Capacity)
                 VALUES (%s, %s)"""
        cursor.execute(sql, (room_name, capacity))
        conn.commit()
        print("Room booked successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while booking room:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Administrative Staff Equipment Maintenance Monitoring
def monitor_equipment_maintenance(equipment_id, last_maintenance_date, next_maintenance_date):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """UPDATE Equipment
                 SET LastMaintenanceDate = %s, NextMaintenanceDate = %s
                 WHERE EquipmentID = %s"""
        cursor.execute(sql, (last_maintenance_date, next_maintenance_date, equipment_id))
        conn.commit()
        print("Equipment maintenance information updated successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while monitoring equipment maintenance:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Administrative Staff Class Schedule Updating
def update_class_schedule(class_id, class_name, trainer_id, room_id, start_time, duration, day_of_week):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """UPDATE ClassSchedule
                 SET ClassName = %s, TrainerID = %s, RoomID = %s, StartTime = %s, Duration = %s, DayOfWeek = %s
                 WHERE ClassID = %s"""
        cursor.execute(sql, (class_name, trainer_id, room_id, start_time, duration, day_of_week, class_id))
        conn.commit()
        print("Class schedule updated successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while updating class schedule:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function for Administrative Staff Billing and Payment Processing
def process_payment(member_id, amount, date, description):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO Billing (MemberID, Amount, Date, Description)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, amount, date, description))
        conn.commit()
        print("Payment processed successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while processing payment:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to display members by search name
def display_members_by_name(search_name):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM Member 
                 WHERE CONCAT(FirstName, ' ', LastName) ILIKE %s"""
        cursor.execute(sql, ('%' + search_name + '%',))
        members_data = cursor.fetchall()
        if len(members_data) == 0:
            print("No members found with the given name.")
        else:
            print("Members with Name containing", search_name)
            for row in members_data:
                print("MemberID:", row[0])
                print("Name:", row[1], row[2])
                print("Email:", row[3])
                print("Address:", row[5])
                print("Phone:", row[6])
                print("----------------------")

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying members by name:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_member_as_json():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM Member"""
        cursor.execute(sql)
        members = cursor.fetchall()

        # Convert data to JSON format
        members_json = []
        for member in members:
            member_data = {
                "MemberID": member[0],
                "FirstName": member[1],
                "LastName": member[2],
                "Email": member[3],
                "Address": member[5],
                "Phone": member[6]
                # Add more fields as needed
            }
            members_json.append(member_data)

        return json.dumps(members_json, indent=4)
    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving members:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Print Tables
def format_table(data):
    if not data:
        print("No data found.")
        return

    # Determine the maximum length of each column
    max_lengths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print table separator
    print('-' * (sum(max_lengths) + len(max_lengths) * 2 - 1))

    # Print table data
    for row in data:
        for value, max_length in zip(row, max_lengths):
            print(str(value).ljust(max_length + 2), end='')
        print()
    print()

if __name__ == '__main__':
    print("\033[1;32mStarting DataBase Access\033[0m")
    sel = ""
    while True:
        if sel == "":
            print("Please Select one of these options:\n\033[1;31m1:Member\033[0m\n\033[1;34m2:Trainer\033[0m\n"
                  "\033[1;35m3:Staff\033[0m\n\033[0;101m4:Exit\033[0m")
            sel = input("->")
        if sel == '1':
            print("\033[4;31mMembers Options:\033[0m\n1:List All members (For Testing purposes)\n"
                  "2:Register a New Member\n3:Display Member Dashboard\n4:Update Member Information\n"
                  "5:Display Health Metrics\n6:Display Fitness Goals\n7:Exit")
            op = input('->')
            if op == '1':
                print("Members Table")
                format_table(list_member())
            elif op == '2':
                print('Please Enter the following info')
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                email = input("Email: ")
                password = input("Password: ")
                address = input("Address: ")
                phone = input("Phone: ")
                register_member(first_name, last_name, email, password, address, phone)
            elif op == '3':
                member_id = input("Please Enter Member ID:\n->")
                display_member_dashboard(member_id)
            elif op == '4':
                member_id = input("Please Enter Member ID:\n->")
                display_member_dashboard(member_id)
                print('Please Update the following info')
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                email = input("Email: ")
                password = input("Password: ")
                address = input("Address: ")
                phone = input("Phone: ")
                update_member_profile(member_id, first_name, last_name, email, password, address, phone)
            elif op == '5':
                member_id = input("Please Enter Member ID:\n->")
                display_health_metrics(member_id)
            elif op == '6':
                member_id = input("Please Enter Member ID:\n->")
                display_fitness_goals(member_id)
            elif op == '7':
                sel = ''
                continue
            else:
                print('Sorry, wrong selection, please try again')
        elif sel == '2':
            print("\033[4;34mTrainer Options:\033[0m\n1:Schedule Management\n2:Search For a memeber")
            op = input('->')
            if op == '1':
                availabilities = [
                    ('08:00:00', '17:00:00', 'Monday'),
                    ('09:00:00', '18:00:00', 'Tuesday'),
                    ('10:00:00', '19:00:00', 'Wednesday'),
                    ('11:00:00', '20:00:00', 'Thursday'),
                    ('08:00:00', '12:00:00', 'Friday')
                ]
                trainer_id = input("Please Enter Trainer ID:\n->")
                set_trainer_availability(trainer_id, availabilities)
            elif op == '2':
                search_name = input("Search for a member by name ")
                display_members_by_name(search_name)
        elif sel == '3':
            print("\033[4;35mStaff Options\033[0m\n1:View Room Bookings\n2:")
        elif sel == '4':
            break
        else:
            print('Sorry, wrong selection, please try again')