import sqlite3
import pandas as pd
print('here')
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('medicine_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for storing medicine information
df=pd.read_csv('Python_GUI\ctk\master_medicine.csv')

df.to_sql('medicines', conn, if_exists='replace', index=False)


conn.commit()

conn.close()


def load_database_file():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine_database.db')

    # Query to select all columns from the medicines table
    query = "SELECT * FROM medicines"

    # Use pandas to read the SQL query result into a DataFrame
    med_df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    return med_df

def load_database():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine_database.db')

    # Query to select all columns from the medicines table
    query = "SELECT * FROM medicines"

    # Use pandas to read the SQL query result into a DataFrame
    med_df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    return med_df      

print(load_database())

def retrieve_medicine_names():
    # Connect to SQLite database
    conn = sqlite3.connect('medicine_database.db')
    cursor = conn.cursor()

    # Retrieve medicine names from the table
    cursor.execute("SELECT Name FROM medicines")
    medicine_names = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    return medicine_names

# Example usage
medicine_names = retrieve_medicine_names()
print("List of Medicines:", medicine_names)
# Commit the changes and close the connection