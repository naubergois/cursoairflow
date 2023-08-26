

from __future__ import annotations
from datetime import datetime, timedelta
from textwrap import dedent


# The DAG object; we'll need this to instantiate a DAG

from airflow import DAG



from airflow.operators.bash import BashOperator


with DAG(

    "alomundo",


    default_args={

        "depends_on_past": False,

        "email": ["airflow@example.com"],

        "email_on_failure": False,

        "email_on_retry": False,

        "retries": 1,

        "retry_delay": timedelta(minutes=5),


    },


    description="Primeira DAG dpo cirso",

    schedule=timedelta(days=1),

    start_date=datetime(2021, 1, 1),

    catchup=False,

    tags=["example"],

) as dag:


    t1 = BashOperator(

        task_id="alomundoyask",

        bash_command="echo 'Alo Mundo' ",

    )



    t1 