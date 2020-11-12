.mode column
select distinct World_region, AVG(MPI_National) 

from MPI_subnational 

where Sub_national_region is not null

group by World_region;


select 'world region' As 'world region', Avg(MPI_national) as 'AVergage MPI national'
from  'MPI_subnational' Group by 'World region', 'country')
Group by 'World region';



