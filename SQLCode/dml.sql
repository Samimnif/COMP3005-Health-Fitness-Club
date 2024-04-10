-- Insert sample data into the Member table
INSERT INTO Member (FirstName, LastName, Email, Password, Address, Phone)
VALUES
('John', 'Doe', 'john@example.com', 'password123', '123 Main St, City', '123-456-7890'),
('Alice', 'Smith', 'alice@example.com', 'pass123', '456 Elm St, Town', '987-654-3210');

-- Insert sample data into the HealthMetrics table
INSERT INTO HealthMetrics (MemberID, Height, Weight, MuscleMass, BPM, DataDate)
VALUES
(1, 180, 80, 50, 70, '2024-04-01'),
(2, 165, 65, 45, 75, '2024-04-03');

-- Insert sample data into the FitnessGoals table
INSERT INTO FitnessGoals (MemberID, Description, GoalWeight, GoalTime, BurnedCalories, TotalSets, TotalReps)
VALUES
(1, 'Lose weight and tone muscles', 160, '00:30:00', 300, 20, 100),
(2, 'Increase strength and endurance', 180, '01:00:00', 500, 30, 150);

-- Insert sample data into the Trainer table
INSERT INTO Trainer (FirstName, LastName, Email, Password, Specialization)
VALUES
('Mike', 'Johnson', 'mike@example.com', 'pass456', 'Strength Training'),
('Sarah', 'Brown', 'sarah@example.com', 'abc123', 'Yoga');

-- Insert sample data into the AdministrativeStaff table
INSERT INTO AdministrativeStaff (FirstName, LastName, Email, Password)
VALUES
('Admin1', 'AdminLastName1', 'admin1@example.com', 'adminpass'),
('Admin2', 'AdminLastName2', 'admin2@example.com', 'admin123');

-- Insert sample data into the Room table
INSERT INTO Room (RoomName, Capacity)
VALUES
('Room A', 20),
('Room B', 15);

-- Insert sample data into the Equipment table
INSERT INTO Equipment (EquipmentName, LastMaintenanceDate, NextMaintenanceDate)
VALUES
('Treadmill', '2023-12-01', '2024-06-01'),
('Dumbbells', '2024-01-15', '2024-07-15');

-- Insert sample data into the ClassSchedule table
INSERT INTO ClassSchedule (ClassName, TrainerID, RoomID, StartTime, Duration, DayOfWeek)
VALUES
('Yoga Class', 2, 1, '08:00:00', 60, 'Monday'),
('Strength Training', 1, 2, '18:00:00', 60, 'Wednesday');

-- Insert sample data into the PersonalTrainingSession table
INSERT INTO PersonalTrainingSession (MemberID, TrainerID, StartTime, Duration)
VALUES
(1, 1, '2024-04-10 09:00:00', 60),
(2, 2, '2024-04-12 17:00:00', 60);

-- Insert sample data into the TrainerAvailability table
INSERT INTO TrainerAvailability (TrainerID, StartTime, EndTime, DayOfWeek)
VALUES
(1, '08:00:00', '17:00:00', 'Monday'),
(1, '09:00:00', '18:00:00', 'Tuesday'),
(1, '10:00:00', '19:00:00', 'Wednesday'),
(1, '11:00:00', '20:00:00', 'Thursday'),
(1, '08:00:00', '12:00:00', 'Friday'),
(2, '10:00:00', '15:00:00', 'Monday'),
(2, '11:00:00', '16:00:00', 'Tuesday'),
(2, '12:00:00', '17:00:00', 'Wednesday'),
(2, '13:00:00', '18:00:00', 'Thursday'),
(2, '14:00:00', '19:00:00', 'Friday');

-- Insert sample data into the Billing table
INSERT INTO Billing (MemberID, Amount, Date, Description)
VALUES
(1, 50.00, '2024-04-01', 'Monthly membership fee'),
(2, 75.00, '2024-04-05', 'Monthly membership fee');
