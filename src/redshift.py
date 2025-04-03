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
    
    def load_jsons(self):
        
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=postgresql port=5435")
        cursor = conn.cursor()
        
        path_json = f"/tmp/{self.table}"
        for name_file in os.listdir(path_json):
            if not name_file.endswith(".json"): 
                continue

            with open(f'/tmp/{self.table}/{name_file}', "r") as f:
                #json_data = f.read()

                with conn.cursor() as cursor:
                    cursor.copy_expert("COPY person_identifier(identifier, identifier_value, person_id) FROM STDIN", f)
                    conn.commit()

