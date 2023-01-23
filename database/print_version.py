# Connect to your database server and print its version


import psycopg2

def get_connection():

    connection = psycopg2.connect(user="postgres",
                                    password="1234",
                                    host="localhost",
                                    port="5432",
                                    database="python_db")
    return connection

def close_connection(connection):
    if connection:  
        connection.close()
def read_database():

    try:
        connection = get_connection()
        cursor=connection.cursor()
        cursor.execute("SELECT version();")
        db_version=cursor.fetchone()
        print(db_version)
        close_connection(connection)

    except(Exception,psycopg2.Error) as error:
        print("Error while getting data", error)

print_data=(read_database())
print(print_data)
