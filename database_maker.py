import MySQLdb

# Replace these with your actual database credentials
host = 'localhost'
user = 'root'
password = 'GoodName[1009]'

# Connect to MySQL
connection = MySQLdb.connect(host=host, user=user, passwd=password)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Replace 'your_database' with the desired database name
database_name = 'job_data'
cursor.execute(f"CREATE DATABASE {database_name}")

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Database '{database_name}' created successfully!")