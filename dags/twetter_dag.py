from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from datetime import datetime

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "jalondono_airflow"
}
with DAG(dag_id="twetter_dag", schedule_interval="@daily", default_args=default_args) as dag:
    waiting4tweets = FileSensor(task_id="waiting4tweets", fs_conn_id="fs_tweet", filepath="data.csv", poke_interval=5)
