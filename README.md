# Python Airflow DAGs Repository

This repository contains Apache Airflow DAGs and supporting files for orchestrating data workflows in Python. It is designed to be used with Docker Compose for local development and testing.

## Repository Structure

- `dags/` - Contains Airflow DAG Python files.
- `plugins/` - Custom Airflow plugins (if any).
- `config/` - Configuration files for Airflow or supporting tools.
- `logs/` - Airflow logs (auto-generated at runtime).
- `docker-compose.yaml` - Docker Compose file to set up Airflow and its dependencies.
- `.env` - Environment variables for Docker Compose.
- `.gitignore` - Git ignore rules.
- `values.yaml` - Additional configuration (possibly for Helm or other tools).

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Running Airflow Locally
1. Clone the repository:
   ```bash
   git clone <this-repo-url>
   cd python-airflow-dags
   ```
2. Start the Airflow services:
   ```bash
   docker-compose up
   ```
3. Access the Airflow web UI at [http://localhost:8080](http://localhost:8080)
   - Default credentials are usually `airflow`/`airflow` (check your `.env` file).

### Adding New DAGs
- Place your DAG Python files in the `dags/` directory. They will be automatically detected by Airflow.

## Example DAGs
- `my_first_dag.py`: A sample DAG to demonstrate Airflow basics.
- `k8s_docker_example.py`: Example DAG for running tasks with Kubernetes or Docker operators.

## Customization
- Modify `docker-compose.yaml` to add or adjust Airflow services.
- Update `.env` for environment-specific settings.

## Kubernetes & Helm Deployment

You can deploy Airflow on Kubernetes using Helm, with DAGs synchronized from this repository using `git-sync`.

### Using `values.yaml`
- The provided `values.yaml` configures Helm to deploy Airflow with the following settings:
  - **DAG Persistence Disabled:** DAGs are not stored on a Persistent Volume Claim (PVC); instead, they are synced from GitHub.
  - **Git-Sync Enabled:**
    - Repository: `https://github.com/rondondaniel/python-airflow-dags.git`
    - Branch: `main`
    - SubPath: `dags` (only the `dags/` folder is used)
    - Syncs every 60 seconds (configurable via `wait`)
  - **Kubernetes Provider:** Installs `apache-airflow-providers-cncf-kubernetes` for KubernetesPodOperator support.

#### Deploying with Helm
1. Install Helm and add the Apache Airflow Helm repo:
   ```bash
   helm repo add apache-airflow https://airflow.apache.org
   helm repo update
   ```
2. Deploy Airflow using your custom `values.yaml`:
   ```bash
   helm install airflow apache-airflow/airflow -f values.yaml
   ```
3. Monitor the deployment and access the Airflow UI (see Helm chart docs for details).

#### Accessing the Airflow UI
- To access the Airflow UI when running in Kubernetes, use port-forwarding:
  ```bash
  kubectl port-forward svc/airflow-webserver 8080:8080
  ```
- Then open [http://localhost:8080](http://localhost:8080) in your browser.
- Default credentials are typically `airflow`/`airflow` (or as set in your Helm values).

### Running KubernetesPodOperator Example
- The DAG `k8s_docker_example.py` demonstrates running a simple Docker image (`hello-world`) as a Kubernetes Pod.
- Once Airflow is running in your Kubernetes cluster (with the Helm chart and `values.yaml`), this DAG will be available in the Airflow UI.
- To trigger the task:
  1. Open the Airflow UI.
  2. Locate the `k8s_docker_example` DAG.
  3. Trigger the DAG manually or set a schedule as needed.
- The task will:
  - Launch a pod in the `airflow` namespace
  - Run the `hello-world` container
  - Delete the pod after completion
  - Stream logs to the Airflow UI

For more details, see the comments in `values.yaml` and `dags/k8s_docker_example.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Last updated: 2025-05-14*
