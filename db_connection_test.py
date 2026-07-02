from database.connection import get_connection

with get_connection() as conn:
    print("Connected!")
