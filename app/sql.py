#! /usr/bin/python3
import pip
from sys import stderr

MYSQL_USER     = 'user'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'website'

try:
    import mysql.connector
except ModuleNotFoundError as e:
    pip.main(['install', "mysql-connector-python"])
    import mysql.connector

class Sql:
    def __init__(self, DB_NAME, DB_HOST='', DB_SOCKET='', DB_USER = "user", DB_PASS = "gvcBz4epRswuuJ"):
        try:
            if DB_HOST != '':
                self.mydb = mysql.connector.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASS,
                    database=DB_NAME,
                    )
            else:
                self.mydb = mysql.connector.connect(
                    unix_socket=DB_SOCKET,
                    user=DB_USER,
                    password=DB_PASS,
                    database=DB_NAME,
                    )

        except Exception as e:
            print("Connection to database failed !\n" + DB_NAME + " is probably not a valid database...\n", file=stderr)
            exit(1)

    def select(self, request):
        """Execute an sql request on the chosen database and return the result"""
        try:
            cursor = self.mydb.cursor()
            cursor.execute(request)
            result = cursor.fetchall()
        except mysql.connector.errors.ProgrammingError as e:
            print(f"Sql request is:\n> {request}", file=stderr)
            raise e
        return result

    def insert(self, request):
        """Execute an sql request on the chosen database and return the result"""
        try:
            cursor = self.mydb.cursor()
            cursor.execute(request)
            self.mydb.commit()
        except mysql.connector.errors.ProgrammingError as e:
            print(f"Sql request is:\n> {request}", file=stderr)
            raise e
