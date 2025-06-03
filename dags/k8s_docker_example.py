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
        task_id="run_docker_image",
        namespace="airflow",
        image="ghcr.io/rondondaniel/python-actoins-test:main",
        cmds=["python", "hello_world.py"],
        container_resources={"node_selectors": {"kubernetes.io/arch": "amd64"}},
        name="run-docker-image",
        on_finish_action="delete_pod",
        in_cluster=True,
        get_logs=True,
    )
