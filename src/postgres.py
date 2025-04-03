from commons.aws.secret_manager import get_secret_key
import logging
from pyspark.sql import DataFrame


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

class Postgres:
    def __init__(self, secret_manager_id, region, table_name, spark):
        self.secret_manager_id = secret_manager_id
        self.region = region
        self.table_name = table_name
        self.credentials_postgres = get_secret_key(
            self.secret_manager_id, self.region)
        self.spark = spark
        self.postgres_url = f"jdbc:postgresql://{self.credentials_postgres['host']}:{self.credentials_postgres['port']}/{self.credentials_postgres['dbname']}"

    def load_data(self, df: DataFrame):

        df.write \
            .format("jdbc") \
            .option("url", self.postgres_url) \
            .option("dbtable", f'api.{self.table_name}') \
            .option("user", self.credentials_postgres['user']) \
            .option("password",self.credentials_postgres['password']) \
            .option("driver", "org.postgresql.Driver") \
            .option("batchsize", "10000") \
            .option("truncate", "true") \
            .mode("overwrite") \
            .save()
        
    

