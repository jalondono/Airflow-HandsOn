from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

# this works because there is a PYTHONPATH ENV variable
import fetching_tweet
import cleaning_tweet

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "jalondono_airflow"
}
with DAG(dag_id="twitter_dag", schedule_interval="@daily", default_args=default_args) as dag:
    waiting4tweets = FileSensor(task_id="waiting4tweets", fs_conn_id="fs_tweet", filepath="data.csv", poke_interval=5)
    fetching_tweets = PythonOperator(task_id="fetching_tweets", python_callable=fetching_tweet.main)
    cleaning_tweets = PythonOperator(task_id="cleaning_tweets", python_callable=cleaning_tweet.main)
