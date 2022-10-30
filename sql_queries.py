# SQL Query To Delete Tables
# Query To Delete airports Table
drop_airports_table = "DROP TABLE IF EXISTS airports;"
# Query To Delete demographics Table
drop_demographics_table = "DROP TABLE IF EXISTS demographics;"
# Query To Delete_table immigrations Table
drop_immigrations_table = "DROP TABLE IF EXISTS immigrations;"
# Query To Delete weather Table
drop_temperature_table = "DROP TABLE IF EXISTS temperature;"

# SQL Query To Create Tables
# Query To Create airports Table
create_airports_table = """
 CREATE TABLE IF NOT EXISTS airports
  (
     iata_code    VARCHAR PRIMARY KEY,
     name         VARCHAR,
     type         VARCHAR,
     local_code   VARCHAR,
     coordinates  VARCHAR,
     city         VARCHAR,
     elevation_ft FLOAT,
     continent    VARCHAR,
     iso_country  VARCHAR,
     iso_region   VARCHAR,
     municipality VARCHAR,
     gps_code     VARCHAR
  );  
"""
# Query To Create demographics Table
create_demographics_table = """
 CREATE TABLE IF NOT EXISTS demographics
  (
     city                   VARCHAR,
     state                  VARCHAR,
     media_age              FLOAT,
     male_population        INT,
     female_population      INT,
     total_population       INT,
     num_veterans           INT,
     foreign_born           INT,
     average_household_size FLOAT,
     state_code             VARCHAR,
     race                   VARCHAR,
     count                  INT
  )
  ;  
"""


# Query To Create immigrations Table
create_immigrations_table = """
 CREATE TABLE IF NOT EXISTS immigrations
  (
     cicid    FLOAT PRIMARY KEY,
     year     FLOAT,
     month    FLOAT,
     cit      FLOAT,
     res      FLOAT,
     iata     VARCHAR,
     arrdate  FLOAT,
     mode     FLOAT,
     addr     VARCHAR,
     depdate  FLOAT,
     bir      FLOAT,
     visa     FLOAT,
     count    FLOAT,
     dtadfile VARCHAR,
     entdepa  VARCHAR,
     entdepd  VARCHAR,
     matflag  VARCHAR,
     biryear  FLOAT,
     dtaddto  VARCHAR,
     gender   VARCHAR,
     airline  VARCHAR,
     admnum   FLOAT,
     fltno    VARCHAR,
     visatype VARCHAR
  );  
"""
# Query To Create temperature Table
create_temperature_table = """
 CREATE TABLE IF NOT EXISTS temperature
  (
     timestamp                       DATE,
     average_temperature             FLOAT,
     average_temperature_uncertainty FLOAT,
     city                            VARCHAR,
     country                         VARCHAR,
     latitude                        VARCHAR,
     longitude                       VARCHAR
  );  
"""
# SQL Query To Insert Data
# Query To Insert Data To airports Table
airport_table_insert = """
             INSERT INTO airports
            (
                iata_code,
                NAME,
                type,
                local_code,
                coordinates,
                city,
                elevation_ft,
                continent,
                iso_country,
                iso_region,
                municipality,
                gps_code
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON conflict
            (
                iata_code
            )
            do nothing"""

# Query To Insert Data To demographics Table
demographic_table_insert = """
 INSERT INTO demographics
            (city,
             state,
             media_age,
             male_population,
             female_population,
             total_population,
             num_veterans,
             foreign_born,
             average_household_size,
             state_code,
             race,
             COUNT)
VALUES      (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# Query To Insert Data To immigrations Table
immigration_table_insert = ("""
 INSERT INTO immigrations
            (
                cicid,
                year,
                month,
                cit,
                res,
                iata,
                arrdate,
                mode,
                addr,
                depdate,
                bir,
                visa,
                count,
                dtadfile,
                entdepa,
                entdepd,
                matflag,
                biryear,
                dtaddto,
                gender,
                airline,
                admnum,
                fltno,
                visatype
            )
            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            ON conflict
            (
                cicid
            )
            do nothing """)

# Query To Insert Data To temperature Table
temperature_table_insert = ("""
 INSERT INTO temperature
            (TIMESTAMP,
             average_temperature,
             average_temperature_uncertainty,
             city,
             country,
               latitude,
             longitude)
VALUES      (%s,%s,%s,%s,%s,%s,%s) """)

# Tables Drop Queries Variables
drop_table_queries = [drop_airports_table, drop_demographics_table,
                      drop_immigrations_table, drop_temperature_table]
# Create Table Queries Variables
create_table_queries = [
    create_airports_table, create_demographics_table, create_immigrations_table, create_temperature_table]
