
import logging
from pyspark.sql import SparkSession
from redshift import Redshift
from postgres import Postgres
import sys 
import json 


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

def handler(config):
    if config.get('POSTGRES_TABLE_NAME') not in ['person_identifier_temp', 'person_information_temp']:
        raise f"Table not expected: {config.get('POSTGRES_TABLE_NAME')}"

    spark = SparkSession.builder \
            .appName("RedshiftToPostgres") \
            .config("spark.jars", "/opt/spark/jars/redshift-jdbc.jar,/opt/spark/jars/postgresql-jdbc.jar") \
            .getOrCreate()
    
    redshift = Redshift(
        secret_manager_id=config.get('REDSHIFT_SECRET_NAME'),
        region=config.get('REGION'),
        table=config.get('REDSHIFT_TABLE_NAME'),
        schema=config.get("REDSHIFT_SCHEMA"),
        spark=spark
    )

    df = redshift.get_full_datas()

    postgres = Postgres(
        secret_manager_id=config.get('POSTGRES_SECRET_NAME'),
        region=config.get('REGION'),
        table_name=config.get('POSTGRES_TABLE_NAME'),
        spark=spark
    )

    postgres.load_data(df=df)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise Exception("There are no argments")

    config = sys.argv[1]
    config = json.loads(config)
    handler(config=config)
