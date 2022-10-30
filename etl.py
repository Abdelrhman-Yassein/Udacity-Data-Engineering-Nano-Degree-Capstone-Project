# Import Libraries
import pandas as pd
import psycopg2 as ps
# Import models
from sql_queries import airport_table_insert, demographic_table_insert, immigration_table_insert, temperature_table_insert
from data_quality_check import check_row_count ,check_row_data

def proccess_temperature_data(cur, conn, file_path):
    """_summary_
        - Read Data
        - Transformation Data
        - Load Data To DataBase
    Args:
        cur (Object): Object To Execute Query
        conn (Object): Connect To DataBase Object
        file_path (String): Data File Path
    """
    # Read Data with reduce  memory usage
    temperature_df = pd.read_csv(file_path, low_memory=False)
    # Select United States Data
    temperature_us_df = temperature_df[temperature_df['Country']
                                       == 'United States']
    # Delete 'AverageTemperature', 'AverageTemperatureUncertainty' Columns
    temperature_us_df = temperature_us_df.dropna(
        subset=['AverageTemperature', 'AverageTemperatureUncertainty'])  # drop all rows with null value
    # delete all dupliacated values and update dataset
    temperature_us_df = temperature_us_df.drop_duplicates(subset=[
                                                          'City', 'dt'])
    # Select Specific Rows Numbers For Reduce Load 
    temperature_us_df = temperature_us_df[:100000]
    # Insert temperature Data Using Insert Sql Query in  'temperature_table_insert' Variable
    try:
        for index, row in temperature_us_df.iterrows():
            cur.execute(temperature_table_insert, list(row.values))
            conn.commit()
    except ps.Error as e:
        print("Error : During Insert Temperature Data ")
        print("Error" + e)


def proccess_demographic_data(cur, conn, file_path):
    """_summary_
            - Read Data
            - Transformation Data
            - Load Data To DataBase
        Args:
            cur (Object): Object To Execute Query
            conn (Object): Connect To DataBase Object
            file_path (String): Data File Path
    """
    # Read Data with reduce  memory sage and delimiter ';'
    demographic_df = pd.read_csv(file_path, delimiter=";", low_memory=False)
    # Drop All Rows With Null Value
    demographic_df.dropna(inplace=True)
    # Insert demographics Data Using Insert Sql Query in  'demographic_table_insert' Variable
    try:
        for index, row in demographic_df.iterrows():
            cur.execute(demographic_table_insert, list(row.values))
            conn.commit()
    except ps.Error as e:
        print("Error : During Insert Demographic Data ")
        print("Error" + e)


def proccess_airports_codes_data(cur, conn, file_path):
    """_summary_
        - Read Data
        - Transformation Data
        - Load Data To DataBase
    Args:
        cur (Object): Object To Execute Query
        conn (Object): Connect To DataBase Object
        file_path (String): Data File Path
    """
    # Read Data with reduce  memory sage
    airport_codes_df = pd.read_csv(file_path, low_memory=False)
    # Get Data Just For Us
    airport_codes_df = airport_codes_df[airport_codes_df['iso_country'] == 'US']
    # Delete Rows With iata_code Null Values
    airport_codes_df.dropna(subset=['iata_code'], inplace=True)
    # Get Port Location 
    df_port_locations = get_port_location()
    # Merge airport_codes_df with df_port_locations
    airport_codes_df = airport_codes_df.merge(
        df_port_locations, left_on="iata_code", right_on="port_code")

    # airport_codes_df.drop(columns=["port_code"], inplace=True)
    airport_codes_df = airport_codes_df[["iata_code", "name", "type", "local_code", "coordinates",
                                         "port_city", "elevation_ft", "continent", "iso_country", "iso_region", "municipality", "gps_code"]]
    # Insert Airports Codes Data Using Insert Sql Query in  'airport_table_insert' Variable
    try:
        for index, row in airport_codes_df.iterrows():
            cur.execute(airport_table_insert, list(row.values))
            conn.commit()
    except ps.Error as e:
        print("Error" + e)


def proccess_immigration_data(cur, conn, file_path):
    # Read Data with reduce  memory usage
    immigration_df = pd.read_csv(file_path, low_memory=False)
    df_port_locations = get_port_location()
    # Get irregular Port
    irregular_ports_df = df_port_locations[df_port_locations["port_city"]
                                           == df_port_locations["port_state"]]
    irregular_ports = list(set(irregular_ports_df["port_code"].values))
    # Delete all irregular ports from immigration_df data
    df_immigration_filtered = immigration_df[~immigration_df["i94port"].isin(
        irregular_ports)]
    # Drop "insnum", "entdepu", "occup", "visapost" Columns
    df_immigration_filtered = df_immigration_filtered.drop(
        columns=["Unnamed: 0", "insnum", "entdepu", "occup", "visapost"])
    # Drop Rows With Null Value
    df_immigration_filtered = df_immigration_filtered.dropna()
    # Insert immigration Data Using Insert Sql Query in  'immigration_table_insert' Variable
    try:
        for index, row in df_immigration_filtered.iterrows():
            cur.execute(immigration_table_insert, list(row.values))
            conn.commit()
    except ps.Error as e:
        print("Error : During Insert immigration Data ")
        print("Error" + e)


def get_port_location():
    # Get port locations from SAS text file
    with open("data/I94_SAS_Labels_Descriptions.SAS") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        ports = content[302:962]
        splitted_ports = [port.split("=") for port in ports]
        port_codes = [x[0].replace("'", "").strip() for x in splitted_ports]
        port_locations = [x[1].replace("'", "").strip()
                          for x in splitted_ports]
        port_cities = [x.split(",")[0] for x in port_locations]
        port_states = [x.split(",")[-1] for x in port_locations]
        df_port_locations = pd.DataFrame(
            {"port_code": port_codes, "port_city": port_cities, "port_state": port_states})
        return df_port_locations


def main():
    run_create_tables = input(
        '\nWould you like to run create_tables.py ? Enter yes or no.\n')
    
    if run_create_tables.lower() != 'yes':
        print("Run create_tables.py...")
        exec(open('create_tables.py').read())

    print("Start Connect To us_immigration DataBase...")
    conn = ps.connect(
        "host=127.0.0.1 dbname=us_immigration user=postgres password=postgre")
    cur = conn.cursor()

    print("Start Proccess temperature Data...")
    proccess_temperature_data(
        cur, conn, 'data/GlobalLandTemperaturesByCity.csv')

    print("Start Proccess Demographic Data...")
    proccess_demographic_data(cur, conn, 'data/us-cities-demographics.csv')

    print("Start Proccess airports Data...")
    proccess_airports_codes_data(cur, conn, 'data/airport-codes_csv.csv')

    print("Start Proccess immigration Data...")
    proccess_immigration_data(cur, conn, 'data/immigration_data_sample.csv')

    print("Check Rows Counts..")
    check_row_count(cur)

    print("Check Rows Data...")
    check_row_data(cur)

    print("Closing Connection....")
    conn.close()

    print("Congratulations, you have successfully completed the ETL Proccess ):")



if __name__ == '__main__':
    main()
