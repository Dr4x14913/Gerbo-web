from sql import *

def login(user, password):
    """TODO: doc"""

    # Connexion to database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)

    # Check username
    if user is None:
        return 0
    if any(char in user for char in " ;"):
        return 0

    # Search in database
    db_pass = db.select(f"Select password from users where username='{user}'")
    if len(db_pass) == 0:
        return 0
    if  db_pass[0][0] == password:
        return user.lower()

    return 0
