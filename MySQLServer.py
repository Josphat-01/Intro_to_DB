import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (update user and password as per your setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # replace with your MySQL username
            password="@Jk12345lm" # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
