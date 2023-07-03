import pyodbc

# Set up connection parameters
server = 'TEACH2C-93918Z8'
database = 'master'
trusted_connection = 'yes'

# Establish a connection
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Define the CREATE TABLE statement
create_table_query = '''
    CREATE TABLE StatsInfo (
        UserID INT,
        Name VARCHAR(50),
        StrengthInfo VARCHAR(50),
    )
    '''

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()