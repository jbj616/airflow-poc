from datetime import datetime
from airflow.sdk import dag, task  

@dag(
    schedule="@daily",
    start_date=datetime(2026, 2, 1),
    catchup=False,
    tags=["example"],
)
def hello_daga():

    @task
    def hello():
        print("AAA Hello, world!")
        return "done"

    @task
    def bye(msg: str):
        print(f"fwfwf{msg}, AAA byebye")

    bye(hello())

hello_daga()
