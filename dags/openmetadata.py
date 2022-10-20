from airflow import DAG
from openmetadata_managed_apis.workflows import workflow_factory

workflow = workflow_factory.WorkflowFactory.create("/opt/bitnami/airflow/dags/postgres_metadata_gxkcihO0.json")
workflow.generate_dag(globals())
dag = workflow.get_dag()