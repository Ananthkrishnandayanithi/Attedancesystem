import sqlite3

def view_submissions():
    # Connect to the SQLite database
    conn = sqlite3.connect('form_submissions.db')
    cursor = conn.cursor()

    # Execute a query to select all records from the submissions table
    cursor.execute("SELECT * FROM submissions")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the column headers
    print("ID\tName\tCourse\tIP Address\tDate")
    print("-" * 50)

    # Print each row in the table
    for row in rows:
        print("\t".join(map(str, row)))

    # Close the connection
    conn.close()

if __name__ == '__main__':
    view_submissions()
