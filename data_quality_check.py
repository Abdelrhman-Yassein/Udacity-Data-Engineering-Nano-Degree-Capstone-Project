# Import Libraries
import psycopg2 as ps


def check_row_count(cur):
    """_summary_
        Query SQL TO Check Rows Number In The Table
    Args:
        cur (Object): Object To Execute Query
    """
    try:
        cur.execute("SELECT COUNT(*) FROM airports;")
        airports = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM demographics;")
        demographics = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM immigrations;")
        immigrations = cur.fetchone()
        cur.execute("SELECT COUNT(*) FROM temperature;")
        temperature = cur.fetchone()
    except ps.Error as e:
        print("Error : Select Count Error From tables")
        print(e)

    print(f"airports Rows count : {airports} \n demographics Rows count : {demographics} \n immigrations Rows count : {demographics} \n temperature Rows count : {demographics} \n")

def check_row_data(cur):
    """_summary_
        Query SQL TO Check Data rows In The Table
    Args:
        cur (Object): Object To Execute Query
    """
    try:
        cur.execute("SELECT * FROM airports LIMIT 5;")
        airports = cur.fetchone()
        cur.execute("SELECT * FROM demographics LIMIT 5;")
        demographics = cur.fetchone()
        cur.execute("SELECT * FROM immigrations LIMIT 5;")
        immigrations = cur.fetchone()
        cur.execute("SELECT * FROM temperature LIMIT 5;")
        temperature = cur.fetchone()
    except ps.Error as e:
        print("Error : Select Count Error From tables")
        print(e)

    print(f"airports Rows Data : {airports} \n demographics Rows Data : {demographics} \n immigrations Rows Data : {demographics} \n temperature Rows Data : {demographics} \n")
