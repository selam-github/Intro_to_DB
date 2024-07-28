import mysql.connector
MySQLServer.pyfrom mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(
            user='root',
            password='Sh238675@Unni.',
            host='local host'
        )
        cursor = cnx.cursor()
        
        # Create the database
        create_database(cursor)
        
        # Close cursor and connection
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if name == "main":
    main()
