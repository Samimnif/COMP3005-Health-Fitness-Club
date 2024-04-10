CREATE TABLE Member (
    MemberID SERIAL,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(20),
  	PRIMARY KEY (MemberID)
);

CREATE TABLE HealthMetrics (
  	HealthMetricID SERIAL,
  	MemberID INT,
  	Height INT,
  	Weight INT,
  	MuscleMass INT,
  	BPM INT,
  	DataDate DATE,
  	PRIMARY KEY (HealthMetricID),
  	FOREIGN KEY (MemberID) REFERENCES Member
);

CREATE TABLE FitnessGoals (
  	GoalID SERIAL,
  	MemberID INT,
  	Description VARCHAR(255),
	GoalWeight INT,
	GoalTime TIME,
	BurnedCalories INT,
	TotalSets INT,
	TotalReps INT,
  	PRIMARY KEY (GoalID),
  	FOREIGN KEY (MemberID) REFERENCES Member
);

CREATE TABLE Trainer (
    TrainerID SERIAL,
    FirstName VARCHAR(255),
 	LastName VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
    Specialization VARCHAR(255),
    PRIMARY KEY (TrainerID)
);

CREATE TABLE AdministrativeStaff (
    StaffID SERIAL,
    FirstName VARCHAR(255),
 	LastName VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
   	PRIMARY KEY (StaffID)
);

CREATE TABLE Room (
    RoomID SERIAL,
    RoomName VARCHAR(255),
    Capacity INT,
   	PRIMARY KEY (RoomID)
);

CREATE TABLE Equipment (
    EquipmentID SERIAL,
    EquipmentName VARCHAR(255),
    LastMaintenanceDate DATE,
    NextMaintenanceDate DATE,
  	PRIMARY KEY (EquipmentID)
);

CREATE TABLE ClassSchedule (
    ClassID SERIAL,
    ClassName VARCHAR(255),
    TrainerID INT,
    RoomID INT,
    StartTime TIME,
    Duration INT,
    DayOfWeek VARCHAR(255),
  	PRIMARY KEY (ClassID),
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID),
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);

CREATE TABLE PersonalTrainingSession (
    SessionID SERIAL,
    MemberID INT,
    TrainerID INT,
    StartTime TIME,
    Duration INT,
  	PRIMARY KEY (SessionID),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
);

CREATE TABLE TrainerAvailability (
    AvailabilityID SERIAL,
    TrainerID INT,
    StartTime TIME,
    EndTime TIME,
    DayOfWeek VARCHAR(255),
    PRIMARY KEY (AvailabilityID),
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
);

CREATE TABLE Billing (
    TransactionID SERIAL,
    MemberID INT,
    Amount DECIMAL(10, 2),
    Date DATE,
  	Description VARCHAR(255),
  	PRIMARY KEY (TransactionID),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);
