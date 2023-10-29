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

#### write_df_to_postgres.py 
writes these 3 dataframes to 3 separate tables located in Postgres server.

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
```


## Airflow Container

You now have a running Airflow container, which can be accessed at [https://localhost:8082](https://localhost:8082).

![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/air.png)

#### Resultant Output

![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/img_exe.png)

### Additional Tables:

1. **First Table**
   
   ![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/post1.png)

2. **Second Table**

   ![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/post2.png)

3. **Third Table**

   ![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/post3.png)

4. **Fourth Table**

   ![Screenshot](https://github.com/2000aliali/Data-Engineering-End-to-End-Project-/blob/main/pos%204.png)














