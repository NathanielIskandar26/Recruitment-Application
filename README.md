# Recruitment-Application
This is a recruitment application built to showcase my skills in Python and PostgreSQL thus far. 
The application allows users to interact with a database of candidates and manage their information, with a purpose to help facilitate a seamless recruitment process.


===APPLICATION OVERVIEW===
An application that stores promising candidates for future recruiting needs.
It displays a list filled with each candidates' attributes, including:
1. Name
2. Gender 
3. Birth year
4. Position
5. Which department is the said position in
6. Asked salary or salary range

The user will be able to:
1. View all entries/candidates.
2. Search entries/candidates based on their attributes listed above.
3. Add entries/candidates.
4. Update selected entries/candidates.
5. Delete selected entries/candidates.
6. Close the application

This application requires all the modules that has been imported in the code  installed in your PC and PostgreSQL to run it properly.
Also, this application will not run without the proper database set up and its credentials.

# Instructions for Running the App:
1. Create a .env file:

2. In the root directory of the project (where the .py file is located), create a new file named db_cred.env

3. Add Your Database Credentials:
Open the .env file and add the following lines, replacing the values with your own PostgreSQL database credentials:

hostname="localhost"

database="your_database_name"

my_username="your_postgres_username"

pwd="your_postgres_password"

port_id=5432

Example:

hostname="localhost"

database="candidates_database"

my_username="postgres"

pwd="your_password_here"

port_id=5432

4. Save the File:
Save the .env file in the root directory of the project.

5. Run the App:
Now, you should be able to run the application without any issues. The app will use the credentials you provided in the .env file to connect to the PostgreSQL database, try adding some data into it!
