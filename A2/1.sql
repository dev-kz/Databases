.mode column
select distinct Country, MPI_Urban, MPI_rural 

from MPI_national 

where MPI_Urban >= 0.1 and MPI_rural >= 0.2;
