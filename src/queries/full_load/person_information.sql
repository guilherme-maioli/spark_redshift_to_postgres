select *
from analytics_prod_dbt_master_data_management_curated.person_information
order by person_id 
LIMIT {limit} OFFSET {offset}