import psycopg2


my_database = psycopg2.connect(user="postgres",
                                    password="1234",
                                    host="localhost",
                                    port="5432",
                                    database="python_db")


cursor=my_database.cursor()
create='CREATE DATABASE python_db'
cursor.execute(create)

my_database.close()
