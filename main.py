from flask import Flask
from flask import render_template, request
import psycopg2
from psycopg2 import OperationalError
from psycopg2 import Error

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Establishing connection 1
connection = create_connection(
    "postgres", "postgres", "1234", "127.0.0.1", "5432"
)

# create_database_query = "CREATE DATABASE numers"
# create_database(connection, create_database_query)

# Establishing connection 2
connection = create_connection(
    "numers", "postgres", "1234", "127.0.0.1", "5432"
)

create_dbusers_table = """
CREATE TABLE IF NOT EXISTS dbusers (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT
);
"""
execute_query(connection, create_dbusers_table)

# USERS!!
# dbusers = [
#     ("Vasya", "Vishnin"),
#     ("Petya", "Zenitkin")
# ]
#
# user_records = ", ".join(["%s"] * len(dbusers))
#
# insert_query = (
#     f"INSERT INTO dbusers (name, surname) VALUES {user_records}"
# )
# print(insert_query)
# connection.autocommit = True
# cursor = connection.cursor()
# cursor.execute(insert_query, dbusers)

# Trying hard to get data back
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * FROM dbusers"
dbusers = execute_read_query(connection, select_users)

for user in dbusers:
    print(user)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

app = Flask(__name__)

users_list = [{'username': 'Jpetrov', 'name': 'John'},
              {'username': 'Pupkin', 'name': 'Vasya'}]

@app.route('/', methods = ['get'])
def index():
    return render_template('site.html')

@app.route('/name/<name>', methods=['get'])
def name_page(name):
    return render_template('site.html', username=name)

@app.route('/users', methods=['get', 'post'])
def users():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        users_list.append({'username': surname, 'name': name})
        # return '<h2> {} {} </h2>'.format(name, surname)
    return render_template('users.html', users=users_list)

if __name__ == '__main__':
    app.run()
