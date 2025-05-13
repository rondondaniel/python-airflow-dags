from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    dag_id="k8s_docker_example",
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    run_docker_image = KubernetesPodOperator(
        namespace="airflow",
        image="hello-world",
        cmds=[],  # hello-world runs its default command, so cmds can be left empty or omitted
        name="run-docker-image",
        task_id="run_docker_image",
        on_finish_action="delete_pod",
        in_cluster=True,
        get_logs=True,
    )
