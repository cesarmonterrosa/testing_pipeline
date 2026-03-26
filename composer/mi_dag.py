from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator

dag_owner = "tu_equipo"

default_args = {
    "owner": dag_owner,
    "depends_on_past": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="move_file_dag",
    default_args=default_args,
    description="DAG para mover archivos vía Dataflow",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dataflow", "gcp"],
) as dag:

    run_dataflow = DataflowTemplatedJobStartOperator(
        task_id="move_file",
        template="gs://my_maincesars-0bucket-200325/templates/movefile",
        project_id="gcp-testing-env2003",
        location="us-central1",
        job_name="move-file-job",
    )