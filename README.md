# Data-Engineering-End-to-End-Project
This ETL (Extract, Transform, Load) project demonstrates the process of getting data from a remote repo , transforming it using L``` PythonL``` , orchestrating the data pipeline withL```  Apache AirflowL```  (running in a L``` Docker containerL``` ), loading the transformed data into  ```PostgreSQL .``` 
## Overview
### THE workflow
![screenshot]()

### Technologies Used
The following technologies and tools were used in this project:

-  Python: For data extraction and transformation.
-   Apache Airflow:  To orchestrate the ETL pipeline.
-   Docker: To run the Apache Airflow instance in a container
-  Pandas: For data manipulation
-  PostgreSQL: Database management system.
-   Psycopg2: To interact with the PostgreSQL database.

### Steps
#### write_csv_to_postgres.py
gets a csv file from a URL. Saves it into the local working directory as churn_modelling.csv. After reading the csv file, it writes it to a local PostgreSQL table

#### create_df_and_modify.py 
reads the same Postgres table and creates a pandas dataframe out of it, modifies it. Then, creates 3 separate dataframes.

##### write_df_to_postgres.py 
writes these 3 dataframes to 3 separate tables located in Postgres server.













In this article, we are going to get a CSV file from a remote repo, download it to the local working directory, create a local ```PostgreSQL``` table, and write this``` CSV ```data to the PostgreSQL table with ``` write_csv_to_postgres.py ```script.

Then, we will get the data from the table. After some modifications and ```pandas ``` practices, we will create 3 separate data frames with the ```create_df_and_modify.py script.```

In the end, we will get these 3 data frames, create related tables in the PostgreSQL database, and insert the data frames into these tables with ```write_df_to_postgres.py ```

To get started, make sure to install the required dependencies using `pip`:

```bash
psycopg
pandas
apache-airflow
datetime
requests
pandasql
urllib3
traceback2
apache-airflow

## The overveux

