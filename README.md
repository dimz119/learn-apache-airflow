# learn-apache-airflow
Apache Airflow 강좌 자료 입니다.

# Notice
airflow.cfg 파일에 <CHANGE TO YOUR LOCATION> 부분을 꼭 바꾸세요

# Installation with standalone
```
# airflow home directory
export AIRFLOW_HOME=~/airflow

export AIRFLOW_VERSION=2.6.2

# Extract the version of Python you have installed. 
# If you're currently using Python 3.11 you may want to set this manually as noted above, 
# Python 3.11 is not yet supported.
export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.6.2 with python 3.7: https://raw.githubusercontent.com/apache/airflow/constraints-2.6.2/constraints-3.7.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# start airflow
airflow standalone
```

# Installation with Docker compose
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

```
# download docker compose file
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.2/docker-compose.yaml'

# start docker compose
docker compose up

$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                    NAMES
79157c05cdf7   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   55 seconds ago   Up 34 seconds (healthy)   8080/tcp                 learn-airflow-airflow-scheduler-1
0f0789d0a5bd   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   55 seconds ago   Up 34 seconds (healthy)   8080/tcp                 learn-airflow-airflow-worker-1
4546e6b49cb0   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   55 seconds ago   Up 33 seconds (healthy)   8080/tcp                 learn-airflow-airflow-triggerer-1
0f3f7a8aa00b   apache/airflow:2.6.2   "/usr/bin/dumb-init …"   55 seconds ago   Up 34 seconds (healthy)   0.0.0.0:8080->8080/tcp   learn-airflow-airflow-webserver-1
fd69ee05eaac   postgres:13            "docker-entrypoint.s…"   55 seconds ago   Up 53 seconds (healthy)   5432/tcp                 learn-airflow-postgres-1
ad7584b994c5   redis:latest           "docker-entrypoint.s…"   55 seconds ago   Up 53 seconds (healthy)   6379/tcp                 learn-airflow-redis-1

# credential
username: airflow / password: airflow

```
