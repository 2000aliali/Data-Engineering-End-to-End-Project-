# Data-Engineering-End-to-End-Project
## Overview
In this article, we are going to get a CSV file from a remote repo, download it to the local working directory, create a local ```PostgreSQL``` table, and write this``` CSV ```data to the PostgreSQL table with ```bash write_csv_to_postgres.py ```script.

Then, we will get the data from the table. After some modifications and ```pandas ``` practices, we will create 3 separate data frames with the```bash
create_df_and_modify.py``` script.

In the end, we will get these 3 data frames, create related tables in the PostgreSQL database, and insert the data frames into these tables with ```bash
write_df_to_postgres.py```

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
apache-airflow```
```
