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

    except (Exception, psycopg2.Error) as error:
        print("Error while displaying member dashboard:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
    return member_data


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
    return health_metrics_data


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
    return fitness_goals_data


# Function for inserting a fitness goal into the database
def insert_fitness_goal(member_id, description, goal_weight, goal_time, burned_calories, total_sets, total_reps):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO FitnessGoals (MemberID, Description, GoalWeight, GoalTime, BurnedCalories, TotalSets, TotalReps)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, description, goal_weight, goal_time, burned_calories, total_sets, total_reps))
        conn.commit()
        print("Fitness goal inserted successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting fitness goal:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Function for inserting a health metric into the database
def insert_health_metric(member_id, height, weight, muscle_mass, bpm, data_date):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """INSERT INTO HealthMetrics (MemberID, Height, Weight, MuscleMass, BPM, DataDate)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (member_id, height, weight, muscle_mass, bpm, data_date))
        conn.commit()
        print("Health metric inserted successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting health metric:", error)
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


def get_schedule(member_id, trainer_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * FROM PersonalTrainingSession 
                 WHERE MemberID = %s AND TrainerID = %s"""
        cursor.execute(sql, (member_id, trainer_id))
        sessions = cursor.fetchall()

        print("Training sessions retrieved successfully!")
        return sessions

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving training sessions:", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


def get_member_personal_session(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT pts.*, t.firstname, t.lastname 
                 FROM PersonalTrainingSession pts
                 INNER JOIN Trainer t ON pts.TrainerID = t.TrainerID
                 WHERE pts.MemberID = %s"""
        cursor.execute(sql, (member_id,))
        sessions = cursor.fetchall()

        print(sessions)
        print("Personal training sessions retrieved successfully!")
        return sessions

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving personal training sessions:", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()


def get_class_registration(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT c.*, cr.dateregistration, t.firstname, t.lastname 
                         FROM ClassSchedule c
                         INNER JOIN ClassRegistration cr ON c.ClassID = cr.ClassID
                         INNER JOIN Trainer t ON c.TrainerID = t.TrainerID
                         WHERE cr.MemberID = %s"""
        cursor.execute(sql, (member_id,))
        classes = cursor.fetchall()
        print(classes)

        print("Class registrations retrieved successfully!")
        return classes

    except (Exception, psycopg2.Error) as error:
        print("Error while retrieving class registrations:", error)
        return None

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


# Function for retrieving trainer information by ID
def get_trainer_info(trainer_id):
    conn = psycopg2.connect(
        database="COMP3005GYM",
        user="postgres",
        password="3005",
        host="localhost",
        port='5432'
    )
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT * FROM Trainer WHERE TrainerID = %s"""
            cursor.execute(sql, (trainer_id,))
            trainer_info = cursor.fetchone()
            return trainer_info
        except psycopg2.Error as e:
            print("Error retrieving trainer information:", e)
        finally:
            if conn:
                conn.close()


# Function for retrieving trainer availabilities by ID
def get_trainer_availabilities(trainer_id):
    conn = psycopg2.connect(
        database="COMP3005GYM",
        user="postgres",
        password="3005",
        host="localhost",
        port='5432'
    )
    if conn:
        try:
            cursor = conn.cursor()
            sql = """SELECT * FROM TrainerAvailability WHERE TrainerID = %s"""
            cursor.execute(sql, (trainer_id,))
            availabilities = cursor.fetchall()
            return availabilities
        except psycopg2.Error as e:
            print("Error retrieving trainer availabilities:", e)
        finally:
            if conn:
                conn.close()


def register_for_class(member_id, class_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        # Check if the member is already registered for the class
        sql_check = "SELECT * FROM ClassRegistration WHERE MemberID = %s AND ClassID = %s"
        cursor.execute(sql_check, (member_id, class_id))
        existing_registration = cursor.fetchone()

        if existing_registration:
            print("Member is already registered for this class.")
            return False

        # Insert new registration
        sql_insert = "INSERT INTO ClassRegistration (MemberID, ClassID, DateRegistration) VALUES (%s, %s, CURRENT_DATE)"
        cursor.execute(sql_insert, (member_id, class_id))
        conn.commit()

        print("Registration for class successfully.")
        return True

    except (Exception, psycopg2.Error) as error:
        print("Error registering for class:", error)
        return False

    finally:
        if conn:
            cursor.close()
            conn.close()


def register_for_personal_session(member_id, trainer_id, time, day, duration):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        # Insert new personal session
        sql_insert = "INSERT INTO PersonalTrainingSession (MemberID, TrainerID, starttime, dayofweek, duration) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql_insert, (member_id, trainer_id, time, day, duration))
        conn.commit()

        print("Personal session booked successfully.")
        return True

    except (Exception, psycopg2.Error) as error:
        print("Error booking personal session:", error)
        return False

    finally:
        if conn:
            cursor.close()
            conn.close()


# Function for Administrative Staff Room Booking Management
def create_room(room_name, capacity):
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
        print("Room created successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while creating room:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Function for Administrative Staff Room Booking Management
def get_rooms():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * 
                FROM Room"""

        cursor.execute(sql)
        rooms = cursor.fetchall()
        return rooms
    except (Exception, psycopg2.Error) as error:
        print("Error while getting room:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def get_trainers():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * 
                FROM Trainer"""

        cursor.execute(sql)
        rooms = cursor.fetchall()
        return rooms
    except (Exception, psycopg2.Error) as error:
        print("Error while getting trainers:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def get_billings():
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * 
                FROM Billing"""

        cursor.execute(sql)
        rooms = cursor.fetchall()
        return rooms
    except (Exception, psycopg2.Error) as error:
        print("Error while getting billing:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def get_member_billing(member_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        sql = """SELECT * 
                FROM Billing
                WHERE MemberID = %s"""

        cursor.execute(sql, (member_id,))
        billings = cursor.fetchall()
        return billings
    except (Exception, psycopg2.Error) as error:
        print("Error while getting member billing:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Function for Administrative Staff Equipment Maintenance Monitoring
def update_equipment_maintenance(equipment_id, last_maintenance_date, next_maintenance_date):
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


# Function to add a new equipment
def add_equipment(name, last_maintenance_date, next_maintenance_date):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()
        sql = """INSERT INTO Equipment (EquipmentName, LastMaintenanceDate, NextMaintenanceDate)
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (name, last_maintenance_date, next_maintenance_date))
        conn.commit()
        print("Equipment added successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error adding equipment:", error)
    finally:
        if conn:
            conn.close()


def get_equipments():
    """Retrieve all equipment from the database."""
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()
        sql = """SELECT * FROM Equipment"""
        cursor.execute(sql)
        equipments = cursor.fetchall()
        return equipments
    except (Exception, psycopg2.Error) as error:
        print("Error retrieving equipment:", error)
    finally:
        if conn:
            conn.close()


def get_classes():
    """Retrieve all class schedules from the database with trainer and room details."""
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()
        sql = """SELECT cs.ClassID, cs.ClassName, t.FirstName, t.LastName, 
                 cs.StartTime, cs.Duration, cs.DayofWeek, r.RoomName
                 FROM ClassSchedule cs
                 INNER JOIN Trainer t ON cs.TrainerID = t.TrainerID
                 INNER JOIN Room r ON cs.RoomID = r.RoomID"""
        cursor.execute(sql)
        classes = cursor.fetchall()
        return classes
    except (Exception, psycopg2.Error) as error:
        print("Error retrieving classes:", error)
    finally:
        if conn:
            conn.close()


# Function to add a new class to the database
def add_class(class_name, trainer_id, room_id, start_time, duration, day_of_week):
    conn = psycopg2.connect(
        database="COMP3005GYM",
        user="postgres",
        password="3005",
        host="localhost",
        port='5432'
    )
    if conn:
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO ClassSchedule (ClassName, TrainerID, RoomID, StartTime, Duration, DayOfWeek)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (class_name, trainer_id, room_id, start_time, duration, day_of_week))
            conn.commit()
            print("Class added successfully!")
        except psycopg2.Error as e:
            print("Error adding class:", e)
        finally:
            if conn:
                conn.close()


def delete_class(class_id):
    """Delete a class from the database."""
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()
        sql = """DELETE FROM ClassSchedule WHERE ClassID = %s"""

        cursor.execute(sql, (class_id,))
        conn.commit()
        print("Class deleted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error deleting class:", error)
    finally:
        if conn:
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

        sql = """INSERT INTO Billing (MemberID, Amount, Date, Description, isPaid)
                 VALUES (%s, %s, %s, %s, 'No')"""
        cursor.execute(sql, (member_id, amount, date, description))
        conn.commit()
        print("Payment processed successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while processing payment:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()


def pay_payment(transaction_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()

        # Update the billing entry to mark it as paid
        sql = """UPDATE Billing 
                 SET ispaid = %s 
                 WHERE transactionid = %s"""
        cursor.execute(sql, ("Yes", transaction_id))

        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error processing payment:", error)
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


def get_staff_info(staff_id):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        if conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM administrativestaff WHERE StaffID = %s"""
            cursor.execute(sql, (staff_id,))
            staff_info = cursor.fetchone()
            return staff_info
    except psycopg2.Error as e:
        print("Error retrieving staff information:", e)
    finally:
        if conn:
            conn.close()

def register_staff(firstname, lastname, email, password):
    try:
        conn = psycopg2.connect(
            database="COMP3005GYM",
            user="postgres",
            password="3005",
            host="localhost",
            port='5432'
        )
        cursor = conn.cursor()
        sql = """INSERT INTO administrativestaff (FirstName, LastName, Email, Password) 
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (firstname, lastname, email, password))
        conn.commit()
        print("Staff registered successfully!")
    except psycopg2.Error as e:
        print("Error registering staff:", e)
    finally:
        if conn:
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
            print("\033[4;34mTrainer Options:\033[0m\n1:Schedule Management\n2:Search For a memeber\n3:Exit")
            op = input('->')
            if op == '1':
                # availabilities = [
                #     ('08:00:00', '17:00:00', 'Monday'),
                #     ('09:00:00', '18:00:00', 'Tuesday'),
                #     ('10:00:00', '19:00:00', 'Wednesday'),
                #     ('11:00:00', '20:00:00', 'Thursday'),
                #     ('08:00:00', '12:00:00', 'Friday')
                # ]
                trainer_id = input("Please Enter Trainer ID:\n->")
                availabilities = []
                start_time = ''
                print('Enter your availability, enter "E" to exit')
                while True:
                    start_time = input("Start Time or 'E' to exit\n->")
                    if start_time == "E":
                        break
                    end_time = input("End Time\n->")
                    day_week = input("Day Week\n->")
                    availabilities.append((start_time, end_time, day_week))

                set_trainer_availability(trainer_id, availabilities)
            elif op == '2':
                search_name = input("Search for a member by name ")
                display_members_by_name(search_name)
            elif op == '3':
                sel = ''
                continue
            else:
                print('Sorry, wrong selection, please try again')
        elif sel == '3':
            print(
                "\033[4;35mStaff Options\033[0m\n1:View Room Bookings\n2:View Classes\n3:View Billing\n4:Register Staff")
            op = input('->')
            if op == '1':
                print("Rooms Table")
                format_table(get_rooms())
            elif op == '2':
                print("Classes Table")
                format_table(get_classes())
            elif op == '3':
                print("Billing Table")
                format_table(get_billings())
            elif op == '3':
                print("Billing Table")
                format_table(get_billings())
            elif op == '4':
                print('Please Enter the following info')
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                email = input("Email: ")
                password = input("Password: ")
                register_staff(first_name, last_name, email, password)
        elif sel == '4':
            break
        else:
            print('Sorry, wrong selection, please try again')
