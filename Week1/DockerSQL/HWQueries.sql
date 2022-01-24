-- Question 3
SELECT distinct count(*) FROM public."yellow_tripdata_2021-01"
where "tpep_pickup_datetime" between '2021-01-15' and '2021-01-16';


-- Question 4
SELECT "tpep_pickup_datetime" FROM public."yellow_tripdata_2021-01" where "tip_amount" = (
    select max(tip_amount) FROM public."yellow_tripdata_2021-01"
    );

-- Question 5
SELECT "DOLocationID", count("DOLocationID") as count FROM public."yellow_tripdata_2021-01"
where "tpep_pickup_datetime" between '2021-01-14' and '2021-01-15'
and "PULocationID" = (select "LocationID" FROM public."taxi+_zone_lookup" where "Zone" = 'Central Park')
group by "DOLocationID" order by count desc limit 1;
-- 237,97

select "Zone" FROM public."taxi+_zone_lookup" where "LocationID" = 237;

-- Question 6
select "PULocationID", "DOLocationID", avg(total_amount) as max FROM public."yellow_tripdata_2021-01"
group by "PULocationID", "DOLocationID" order by max desc;

select "Zone" FROM public."taxi+_zone_lookup" where "LocationID" in (4,265);