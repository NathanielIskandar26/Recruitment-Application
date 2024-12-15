#APP VER 1.0.0
#
#===APPLICATION OVERVIEW===
#An application that stores promising candidates for future recruiting needs.
#It displays a list filled with each candidates' attributes, including:
#1. Name
#2. Gender 
#3. Birth year
#4. Position
#5. Which department is the said position in
#6. Asked salary or salary range
#
#The user will be able to:
#1. View all entries/candidates.
#2. Search entries/candidates based on their attributes listed above.
#3. Add entries/candidates.
#4. Update selected entries/candidates.
#5. Delete selected entries/candidates.
#6. Close the application


import psycopg2
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='db_cred.env')

def create_table():
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    create_table_script = '''CREATE TABLE IF NOT EXISTS candidate(
                        candidate_id        SERIAL PRIMARY KEY,
                        name                VARCHAR(50) NOT NULL,
                        gender              VARCHAR(10),
                        birth_year          VARCHAR(4),
                        position            VARCHAR(80) NOT NULL,
                        department          VARCHAR(80),
                        asked_salary_range  VARCHAR(40) NOT NULL
                        )'''
    cur.execute(create_table_script)
    conn.commit()
    conn.close()

def add_entry(name, gender, birth_year, position, department, asked_salary_range):
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    add_entry_script = '''INSERT INTO candidate(
                        name, gender, birth_year, position, department, asked_salary_range) 
                        VALUES(%s,%s,%s,%s,%s,%s)'''
    record_to_insert = (name, gender, birth_year, position, department, asked_salary_range)
    cur.execute(add_entry_script, record_to_insert)
    conn.commit()
    conn.close()

def view_entry():
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    view_entry_script = '''SELECT * FROM candidate ORDER BY candidate_id'''
    cur.execute(view_entry_script)
    rows=cur.fetchall()
    conn.close()
    return rows

def search_entry(name="", gender="", birth_year="", position="", department="", asked_salary_range=""):
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    search_entry_script = '''SELECT * FROM candidate
                        WHERE (name ILIKE %s OR %s IS NULL) 
                        AND (gender ILIKE %s OR %s IS NULL) 
                        AND (birth_year ILIKE %s OR %s IS NULL) 
                        AND (position ILIKE %s OR %s IS NULL) 
                        AND (department ILIKE %s OR %s IS NULL) 
                        AND (asked_salary_range ILIKE %s OR %s IS NULL)'''
    record_to_search = (
        '%' + name + '%', name,
        '%' + gender + '%', gender,
        '%' + birth_year + '%', birth_year,
        '%' + position + '%', position,
        '%' + department + '%', department,
        '%' + asked_salary_range + '%', asked_salary_range
    )
    cur.execute(search_entry_script, record_to_search)
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_entry(id):
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    delete_entry_script = f"DELETE FROM candidate WHERE candidate_id = {id}"
    cur.execute(delete_entry_script)
    conn.commit()
    conn.close()

def update_entry(id, name, gender, birth_year, position, department, asked_salary_range):
    conn = psycopg2.connect(
        host = os.getenv('hostname'),
        dbname = os.getenv('database'),
        user = os.getenv('my_username'),
        password = os.getenv('pwd'),
        port = os.getenv('port_id')
        )
    cur = conn.cursor()
    update_entry_script = '''UPDATE candidate SET name = %s, gender = %s, 
                            birth_year = %s, position = %s, department = %s, 
                            asked_salary_range = %s WHERE candidate_id = %s'''
    record_to_update = (name, gender, birth_year, position, department, asked_salary_range, id)
    cur.execute(update_entry_script, record_to_update)
    conn.commit()
    conn.close()

create_table()
