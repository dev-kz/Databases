.mode column
select distinct World_region, AVG(MPI_Urban), AVG(MPI_rural)

from MPI_subnational inner join MPI_national

on MPI_national.ISO = MPI_subnational.ISO 
	and Sub_national_region is not null

group by World_region; 