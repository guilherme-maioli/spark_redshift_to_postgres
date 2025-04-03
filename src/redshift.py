from commons.aws.secret_manager import get_secret_key
import logging

from typing import Dict
import json

from pyspark.sql import DataFrame
import os 
import json
import psycopg2


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


class Redshift:
    def __init__(self, secret_manager_id, region, table, schema, spark):
        self.secret_manager_id = secret_manager_id
        self.region = region
        self.credentials_redshift = get_secret_key(
            self.secret_manager_id, self.region)
        self.schema = schema
        self.table = table
        self.redshift_url = f"jdbc:redshift://{self.credentials_redshift['host']}:{self.credentials_redshift['port']}/{self.credentials_redshift['db_name']}"
        self.spark = spark
        self.redshift_properties = {
            "user": self.credentials_redshift['username'],
            "password": self.credentials_redshift['password'],
            "driver": "com.amazon.redshift.jdbc.Driver"
        }

    def get_full_datas(self) -> Dict:
        logging.info('Get Data')
        df = self.spark.read.jdbc(
            url=self.redshift_url, 
            table=f"{self.schema}.{self.table}", 
            properties=self.redshift_properties
        )
        
        return df
    

