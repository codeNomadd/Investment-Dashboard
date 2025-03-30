import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to create the `portfolios` table
def create_portfolios_table():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS portfolios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                symbol VARCHAR(10) NOT NULL,
                quantity DECIMAL(10, 2) NOT NULL,
                purchase_price DECIMAL(10, 2) NOT NULL
            )
            """)
            connection.commit()
            print("Portfolios table created successfully!")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

# Call the function to create the table
if __name__ == "__main__":
    create_portfolios_table()
