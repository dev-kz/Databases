.mode column
select distinct MPI_national.Country, MPI_Urban, MPI_rural, MPI_National 

from MPI_national inner join MPI_subnational

on MPI_national.ISO = MPI_subnational.ISO 
	and MPI_Urban >= 0.1 and MPI_rural >= 0.2 
	and MPI_National is not null

order by MPI_National ASC;