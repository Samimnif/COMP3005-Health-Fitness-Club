# COMP 3005 - Winter 2024- Project: Health and Fitness Club Management System

## Author

Sami Mnif - 101199669

## Description

The Project is written in python, using the Flask library to run a local webserver.
There are two main components in this project:

1. `database_access.py`: is a python file that contains lots of getter and setter functions that allows me to access the
   database and modify it accordingly. This file also conatins the command line program that gives you an option to
   really quickly access the database through the command line. Although not all functions are implemented in the
   command line program. You can still find the other functions in teh webserver.
2. `main.py`: this python file, starts the flask server in the local port 5000 and will display a website. You can
   navigate through the webserver using the nav bar. You can register a member and access their data.

* To Test the Command line: run `database_access.py`.
* To Test the Webserver: run `main.py`

## Table Creation

Use the ddl.sql file under the /SQLCode folder to create the needed tables for this project
Then use the dml.sql file to insert sample data to manipulate with the functional methods.

## Demo Link

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/quCgDmJowH4/0.jpg)](https://youtu.be/quCgDmJowH4?si=bSUWdujCsxDQ1cK4)

## Implementation Description

For this project, I created a web app in Python using Flask. I have two Python files in the project folder.<br>
main.py hosts the flask webserver that implements all the web page routes and accesses the data either directly in the
routing functions or using one of the defined functions in the database_access.py file.<br>
database_access.py file contains a lot of defined setter and getter functions that are used in both the Webserver in
main.py and in the command line tool that is also available in the database_access.py file (Under the main section at
the bottom of the file).<br>
Most of the functions are used in the Webserver. My focus in this project was the website UI. I included functions like
Member registration, Member Login, Trainer Login, and Staff Login.
<br>
The Members can see their dashboard and profile. They can update their profile info and add Health Metrics and Fitness
Goals to their dashboard. There is also a section for Billing and payment. Whenever they attend a class or personal
session, the Staff would send a Billing Payment Request to the Member Account. The member then can pay using their
payment Card. In the classes tab, Members can schedule, reschedule or cancel personal sessions with Trainers and they
can register/unregister for a class.
<br>
The Trainers have their dashboard where they can check their availability schedule and they can update and adjust it.
They have access to the member directory list, and they can search by name, last name or member ID. Each member in that
list has a link that the trainer can press to reveal the Member profile information and the scheduled session that they
booked with that specific trainer.
<br>
We are assuming here that the Trainer and the Member do agree on a time and date beforehand, but either way, the system
does check if the selected personal session daytime is within the selected Trainer's availability.
<br>
The Admin Staff have also their own dashboard, they can access the Equipment list and see the last time was serviced and
the next time it should be serviced (we are assuming that the system will use that date to send a notification to staff
emails). The Staff also can delete and add classes to the class list (this will adjust the class list options that the
members can select). Staff can also check all billing transactions of all members, and they can process a billing by
assigning an invoice to their account so that they pay for it from their account.
<br>
We are assuming here that the only way the Gym accepts payments is through the website through personal accounts. The
billing happens manually since it pays as you use kind of a Gym (the staff will manage the transactions).

<hr>

# Copyright
© Copyright 2024 Sami Mnif