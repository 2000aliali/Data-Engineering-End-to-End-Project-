import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# Determine the path to the parent directory
parent_folder = os.path.dirname(os.path.abspath(__file__))
scripts_folder = os.path.join(parent_folder, 'dags')

# Add the 'python_scripts' folder to the system path
if scripts_folder not in sys.path:
    sys.path.append(scripts_folder)
#parent_folder = os.path.dirname(os.path.abspath(__file__))
#scripts_folder = os.path.join(parent_folder, 'python_scripts')

from python_scripts.write_csv_to_postgres import write_csv_to_postgres_main
from python_scripts.write_df_to_postgres import write_df_to_postgres_main
# ... rest of your DAG code ...
start_date = datetime(2023, 10, 28, 18, 34)

default_args = {
    'owner': 'dogukanulu',
    'start_date': start_date,
    'retries': 5,
    'retry_delay': timedelta(seconds=5)
}

with DAG('csv_extract_airflow_docker', default_args=default_args, schedule='@daily') as dag:




    

    write_csv_to_postgres = PythonOperator(
        task_id='write_csv_to_postgres',
        python_callable=write_csv_to_postgres_main,
        retries=1,
        retry_delay=timedelta(seconds=15))

    write_df_to_postgres = PythonOperator(
        task_id='write_df_to_postgres',
        python_callable=write_df_to_postgres_main,
        retries=1,
        retry_delay=timedelta(seconds=15))
    
    write_csv_to_postgres >> write_df_to_postgres 