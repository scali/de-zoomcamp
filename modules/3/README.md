```sql
-- External table
CREATE OR REPLACE EXTERNAL TABLE `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata`
OPTIONS (
    format = 'PARQUET',
    uris = ['gs://de-zoom-camp-412008-mage-bucket/green_taxi_ny/green_tripdata_2022-*.parquet']
);
```


```sql
-- Query for question #1
SELECT count(*) FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata
```


```sql
-- Materialized Table from the external table
CREATE OR REPLACE TABLE `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_nonpartitioned`
AS SELECT * FROM `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata`;
```

```sql
-- Query for question #2
SELECT count(distinct(PULocationID)) FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata

SELECT count(distinct(PULocationID)) FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_nonpartitioned
```

```sql
-- Query for question #3
SELECT count(*) FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata WHERE fare_amount = 0
```

```sql
-- Query for question #4
CREATE OR REPLACE TABLE `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(TIMESTAMP_MILLIS(lpep_pickup_datetime))
CLUSTER BY PUlocationID AS (
    SELECT * FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_nonpartitioned
);

-- Query for question #4 if we omit the timestamp casting during the data load :-S
CREATE OR REPLACE TABLE `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime_cast)
CLUSTER BY PUlocationID AS (
    SELECT *, TIMESTAMP_MILLIS(CAST((lpep_pickup_datetime/1000000) AS INT64)) as lpep_pickup_datetime_cast FROM de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_nonpartitioned
);
```


```sql
-- Queries for question #5
SELECT count(distinct(PULocationID)) FROM `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_nonpartitioned`
WHERE DATE(TIMESTAMP_MILLIS(CAST((lpep_pickup_datetime/1000000) AS INT64))) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT count(distinct(PULocationID)) FROM `de-zoom-camp-412008.ny_taxi.external_yellow_tripdata_partitioned_clustered`
WHERE DATE(lpep_pickup_datetime_cast) BETWEEN '2022-06-01' AND '2022-06-30';
```


