from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models.param import Param

with DAG(dag_id='airbyte',
         default_args={'owner': 'airflow'},
         schedule_interval='*/5 * * * *',
         start_date=days_ago(1),
         params={"connection_id_param": Param("", type="string")}
    ) as dag:

    airbyte_trigger_sync_operator = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync',
        airbyte_conn_id='air_byte_connection',
        connection_id="93c215f7-9063-41d3-a47c-9f2a1363513f",
        asynchronous=False,
        timeout=20000,
        wait_seconds=3
    )