# Import Libraries
import psycopg2 as ps
# import Sql Query Model , Create and Drop Queries Statment Variables
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """_summary_
       1 -Connect To Udacity Default DataBase To Create Database
       2 -Drop us_immigration Database If exists
       3 -Create us_immigration Database
    Returns:
       conn ->  Object: Connect to Database Object
       cur  ->  Object: Object To Execute SQL Query
    """
    # us_immigration

    # connect to default database
    """_summary_
        dbname   ->  DateBase Default Name
        user     ->  DateBase User Name
        password ->  DateBase User Password
    """
    # Connect to Default DataBase
    conn = ps.connect(
        "host=127.0.0.1 dbname=udacity user=postgres password=postgre")
    # Session Auto Commit
    conn.set_session(autocommit=True)
    # Create cur Object To Run Query Statment
    cur = conn.cursor()

    # Drop us_immigration Table If Exists
    cur.execute("DROP DATABASE IF EXISTS us_immigration")
    # Create us_immigration DataBase with UTF8 encoding
    cur.execute(
        "CREATE DATABASE us_immigration WITH ENCODING 'utf8' TEMPLATE template0")

    # Close Connection to Default DataBase
    conn.close()

    # Connect To us_immigration DataBase
    conn = ps.connect(
        "host=127.0.0.1 dbname=us_immigration user=postgres password=postgre")
    # Create cur Object To Run Query Statment
    cur = conn.cursor()
    # return cur and conn Object
    return cur, conn


def drop_tables(cur, conn):
    """_summary_
        Drop Table Query Statements From  'drop_table_queries'
    Args:
        cur (Object): Connect to Database Object
        conn (Object): Object To Execute SQL Query
    """
    # For Loop For Run All Queries In Variable
    try:
        for query in drop_table_queries:
            cur.execute(query)  # Run Query
            conn.commit()      # Commit Query
    except ps.Error as e:
        print("Error During Drop Tables")
        print("Error : " + e)            


def create_tables(cur, conn):
    """_summary_
        Create Table Query Statements From  'create_table_queries'
    Args:
        cur (Object): Connect to Database Object
        conn (Object): Object To Execute SQL Query
    """
    # For Loop For Run All Queries In Variable
    try:
        for query in create_table_queries:
            cur.execute(query)  # Run Query
            conn.commit()      # Commit Query
    except ps.Error as e:
        print("Error During Create Tables")
        print("Error : " + e)        


def main():
    """_summary_
        1 - Create us_immigration DataBase
            - Connect To Default DataBase
            - Drop DataBase If Exists
            - Create us_immigration DataBase
            - Return cur and conn Objects

        2 - Drop All Tables If Exists
        3 - Create New Tables
        4 - Close Connection            
    """
    """
        Create New Data Base And return cur and conn Objects
        conn ->  Object: Connect to Database Object
        cur  ->  Object: Object To Execute SQL Query
    """
    print("Create New DataBase...")
    cur, conn = create_database()

    # Drop All Tables Use conn and cur Objects
    print("Drop Tables If Exists...")
    drop_tables(cur, conn)
    # Create All Tables Use conn and cur Objects
    print("Create New Tables...")
    create_tables(cur, conn)
    # Close Connection
    print("Close Connection...")
    conn.close()


if __name__ == "__main__":
    print("Start Create Database and Tables...")
    main()
    print("Congratelaution, Finished Create DataBase And Tables.. ): ")
