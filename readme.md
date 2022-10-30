# Udacity Data Engineering Capstone Project

In this project, we will be looking at the immigration data for the united states
## DataSets

### 1 - I94 Immigration Data:
This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace. .[this](https://travel.trade.gov/research/reports/i94/historical/2016.html) is where the data comes from. There's a sample file so you can take a look at the data in csv format before reading it all in. You do not have to use the entire dataset, just use what you need to accomplish the goal you set at the beginning of the project.

### 2 - World Temperature Data: 
This dataset came from Kaggle. You can read more about it [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data) .

### 3 - U.S. City Demographic Data: 
This data comes from OpenSoft. You can read more about it [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/) .

### 4 - Airport Code Table: 
This is a simple table of airport codes and corresponding cities. It comes from  [here](https://datahub.io/core/airport-codes#data) .


The project follows the follow steps:
* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up

## Conceptual Data Model

### Tables:

# 1 - Immigrations - Fact Table

* `1-cicid 2-year 3-month 4-cit 5-res `
* `6-iata 7-arrdate 8-mode 9-addr 10-depdate `
* `11-bir 12-visa 13-coun 14-dtadfil 15-visapost `
* `16-occup 17-entdepa 18-entdepd 19-entdepu`
* `20-matflag 21-biryear 22-dtaddto 23-gender 24-insnum 25-airline`
* `26-admnum 27-fltno 28-visatype`

# 2 - Airports - Dimension Table

* 1 - `iata_code`
* 2 - `name` 
* 3 - `type` 
* 4 - `local_code` 
* 5 - `coordinates` 
* 6 - `city` 

# 3 - Demographics - Dimension Table

* 1  - `city`
* 2  - `state` 
* 3  - `media_age` 
* 4  - `male_population` `
* 5  - `female_population` 
* 6  - `total_population` 
* 7  - `num_veterans` 
* 8  - `foreign_born` 
* 9  - `average_household_size` 
* 10 - `state_code` 
* 11 - `race` 
* 12 - `count` 

# 4 - Temperature - Dimension Table

* 1  - `timestamp`
* 2  - `average_temperature` 
* 3  - `average_temperatur_uncertainty` 
* 4  - `male_population` `
* 5  - `city` 
* 6  - `country` 
* 7  - `latitude` 
* 8  - `longitude` 





## Mapping Out Data Pipelines
#### 1 - Extract Data
#### 2 - Describe and Show Data 
#### 3 - Transformation Data 
#### 4 - Run create_tables.py 
#### 5 - Load Data Into DataBase 

## files and folders
#### 1 - data folder -> Contain all Data File
#### 2 - Capstone Project Template.ipynb  -> ipynb project file
#### 3 - create_tables.py -> file To Create DataBase And Tables you can run ` python create_tables.py`
#### 4 - data_quality_check.py -> To check data after load 
#### 5 - sql_queries.py -> Contain all sql queries we need to create and drop tables and insert

## How To Run Project
    1 - You Must Update All Username and Passwrod for your Database
    2 - Capstone Project Template.ipynb -> Just Run Cel
    3 - etl.py in cmd 'python etl.py'



## Contact

## **Abdelrhman Yassein  :**  [LinkedIn](https://www.linkedin.com/in/Abdelrhman-Yassein/) - [GitHub](https://github.com/Abdelrhman-Yassein?tab=repositories)

