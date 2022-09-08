from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

with DAG(dag_id='trigger_airbyte_job_example',
         default_args={'owner': 'airflow'},
         schedule_interval='*/5 * * * *',
         start_date=days_ago(1)
    ) as dag:

    money_to_json = AirbyteTriggerSyncOperator(
        task_id='airbyte_money_json_example',
        airbyte_conn_id='air_byte_connection',
        connection_id='8ea1a0c5-c6c6-4553-988c-9f2dc95bebe3',
        asynchronous=False,
        timeout=20000,
        wait_seconds=3
    )