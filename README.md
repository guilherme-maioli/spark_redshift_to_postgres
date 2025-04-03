# Redshift to PostgreSQL Data Transfer

## Overview
This project facilitates the transfer of data from Amazon Redshift to PostgreSQL using Apache Spark (PySpark). It securely retrieves database credentials from AWS Secrets Manager and supports full data loads from Redshift tables (`person_identifier` or `person_information`) into corresponding temporary tables in PostgreSQL. The project is designed for scalability and ease of use in data pipeline workflows.

## Features
- Transfers data from Redshift to PostgreSQL using PySpark.
- Secure credential management via AWS Secrets Manager.
- Supports full data loads with overwrite mode.
- Organized SQL queries for full, incremental, and test scenarios.

## Project Structure
```
src/
├── main.py                   # Main script to orchestrate data transfer
├── postgres.py               # PostgreSQL connection and data loading
├── redshift.py               # Redshift connection and data retrieval
├── commons/aws/              # AWS utility modules
│   └── secret_manager.py     # AWS Secrets Manager credential retrieval
├── jars/                     # Directory for JDBC drivers
└── queries/                  # SQL queries
    ├── full_load/            # Full load queries
    ├── incremental/          # Incremental load queries
    └── testes/               # Test scripts
```

## Prerequisites
- Python 3.x
- PySpark
- AWS SDK (`boto3`)
- `psycopg2`
- JDBC Drivers:
  - `redshift-jdbc.jar`
  - `postgresql-jdbc.jar`
- AWS Credentials with Secrets Manager access

## Setup
### Clone the Repository:
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```
### Install Dependencies:
```bash
pip install pyspark boto3 psycopg2-binary
```
### Add JDBC Drivers:
- Download `redshift-jdbc.jar` and `postgresql-jdbc.jar`.
- Place them in `src/jars/` or update the path in `main.py` (default: `/opt/spark/jars/`).

### Configure AWS:
Set up AWS credentials:
```bash
aws configure
```
Create Secrets Manager secrets for Redshift and PostgreSQL credentials (e.g., host, port, username, password, etc.).

### Install Spark:
Ensure Spark is installed and accessible via `spark-submit`.

## Usage
Run the script with `spark-submit` and a JSON configuration:

```bash
spark-submit src/main.py '{
    "REDSHIFT_SECRET_NAME": "<secret_with_credencials_redshift>",
    "REGION": "<region_aws>",
    "POSTGRES_SECRET_NAME": "<secret_with_credencials_postgres>",
    "POSTGRES_TABLE_NAME": "<name_of_table_in_postgres>",
    "REDSHIFT_SCHEMA": "<schema_source_in_reshift>",
    "REDSHIFT_TABLE_NAME": "<table_source_in_reshift>"
}'
```

### Example
```bash
spark-submit src/main.py '{
    "REDSHIFT_SECRET_NAME": "prod/redshift/credentials",
    "REGION": "us-east-1",
    "POSTGRES_SECRET_NAME": "prod/postgres/credentials",
    "POSTGRES_TABLE_NAME": "person_identifier_temp",
    "REDSHIFT_SCHEMA": "analytics_prod_dbt_master_data_management_curated",
    "REDSHIFT_TABLE_NAME": "person_identifier"
}'
```

## Configuration Parameters
| Parameter                | Description                                     | Example Value |
|--------------------------|-------------------------------------------------|---------------|
| `REDSHIFT_SECRET_NAME`   | Secret name for Redshift credentials           | `prod/redshift/credentials` |
| `REGION`                 | AWS region                                     | `us-east-1` |
| `POSTGRES_SECRET_NAME`   | Secret name for PostgreSQL credentials         | `prod/postgres/credentials` |
| `POSTGRES_TABLE_NAME`    | Target table (must be `person_identifier_temp` or `person_information_temp`) | `person_identifier_temp` |
| `REDSHIFT_SCHEMA`        | Source schema in Redshift                      | `analytics_prod_dbt_master_data_management_curated` |
| `REDSHIFT_TABLE_NAME`    | Source table in Redshift                       | `person_identifier` |

## How It Works
1. Validates the `POSTGRES_TABLE_NAME`.
2. Initializes a Spark session with JDBC drivers.
3. Retrieves data from Redshift into a DataFrame.
4. Writes the DataFrame to PostgreSQL, overwriting existing data in the `api` schema.

## SQL Queries
- **Full Load**: `queries/full_load/` - Retrieves all data from Redshift tables.
- **Incremental**: `queries/incremental/` - For incremental updates (not used in main flow).
- **Tests**: `queries/testes/` - Scripts for creating tables, views, and sample data.

## Troubleshooting
- **JAR Errors**: Ensure JDBC drivers are in the specified path.
- **AWS Errors**: Verify credentials and Secrets Manager permissions.
- **Table Name Errors**: Use only `person_identifier_temp` or `person_information_temp`.

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, open an issue or reach out to the maintainers.
