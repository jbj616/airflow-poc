from datetime import datetime
from airflow.sdk import dag, task  

@dag(
    schedule="@daily",
    start_date=datetime(2026, 2, 1),
    catchup=False,
    tags=["example"],
)
def hello_dag2():

    @task
    def hello():
        print("FWFWF Hello, world!")
        return "done"

    @task
    def bye(msg: str):
        print(f"fwfwf{msg}, byebye")

    bye(hello())

hello_dag2()
