# Hospital_Management_System
Our Hospital Management System is a simple and effective implementation of all the various functionalities of a hospital. This system would provide you with all the information that you need to know about the working of a hospital.
HMS would empower you with easy access to essential information about the hospital, its staff and patients that you need to know.

## FUNCTIONALITIES
- Provides a user friendly environment for patients and hospital staff
- Stores all essential details regarding the hospital
- Automatic and dynamic updation of database
- Provides an overview about the hospital, its staff and patients


## Technologies Used
- Python  Web Framework - DJANGO
- Database management system - MYSQL
- Front End development tools - HTML , JAVASCRIPT , CSS,JQUERY,BOOTSTRAP


## How it works
The website  uses html , css  and javascript to enhance the front end providing necessary graphical illustrations. The backend which deals with the management of  the database is done using Mysql. 
The interconnection between the two is done by Django which is python based web framework.
Details about the doctors, nurses and patients are entered manually. Updation of corresponding tables is done dynamically. Initially there is a login page available . Users need to login to access  the rest of the information. 


## Basic Architecture includes
1. To create a Doctor | Department | Nurse
2. To admit a Patient | Emergency
3. To create database relationship between Departments ,Doctors ,Nurses ,patients ,Emergency tables
4. To list the patients | doctors in a department
5. To get the nurses /doctors in a hostpital

# How to start
1. Open a terminal
2. Create a virtual env - python3 -m venv {envname} . eg:python3 -m venv djangenv
3. Activate virtual Environment - source djangenv/bin/activate
4. pip3 install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. Microservice will be running at port 8000 by default
9. You can go to http://127.0.0.1:8000/ andf perform the required functionalities in a hospital as mentioned above


## Enhancements that can be made
1. Create ER Diagram using Proper Web Tools
2. A lot of imporvements can be made in terms of form Validation
3. UI can migrated to Angular or React from DTL
4. Deployment to Cloud Frameworks
5. UX Experience can be improved a lot