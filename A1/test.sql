CREATE TABLE MPI_national(
	ISO TEXT NOT NULL,

	Country TEXT,

	MPI_urban NUMERIC CHECK(MPI_urban IS 'MPI Urban' OR
	 						MPI_urban >= 0 AND MPI_urban <= 1),

	Headcount_urban NUMERIC CHECK(Headcount_urban IS 'Headcount Ratio Urban' OR
								  Headcount_urban >= 0 AND Headcount_urban <= 100),

	Intensity_urban NUMERIC CHECK(Intensity_urban IS 'Intensity of Deprivation Urban' OR 
								  Intensity_urban >= 0 AND Intensity_urban <= 100),

	MPI_rural NUMERIC CHECK(MPI_rural IS 'MPI Rural' OR
							MPI_rural >= 0 AND MPI_rural <= 1),

	Headcount_rural NUMERIC CHECK(Headcount_rural IS 'Headcount Ratio Rural' OR 
								  Headcount_rural >= 0 AND Headcount_rural <= 100),

	Intensity_rural NUMERIC CHECK(Intensity_rural IS 'Intensity of Deprivation Rural' OR
								  Intensity_rural >= 0 AND Intensity_rural <= 100), 

	PRIMARY KEY(ISO)
);


CREATE TABLE MPI_subnational(
	ISO TEXT NOT NULL,

	Country TEXT,

	Subnational TEXT CANDIDATE KEY NOT NULL,

	World_region TEXT CHECK(World_region IS 'World region' OR 
							World_region IS 'Sub-Saharan Africa' OR 
							World_region IS 'Latin America and Caribbean' OR 
							World_region IS 'East Asia and the Pacific' OR 
							World_region IS 'Arab States' OR 
							World_region IS 'South Asia' OR 
							World_region IS 'Europe and Central Asia'),

	MPI_national NUMERIC CHECK(MPI_national IS 'MPI National' OR
							   MPI_national >= 0 AND MPI_national <= 1),

	MPI_regional NUMERIC CHECK(MPI_regional IS 'MPI Regional' OR
							   MPI_regional >= 0 AND MPI_regional <= 1),

	Headcount NUMERIC CHECK(Headcount IS 'Headcount Ratio Regional' OR
							Headcount >= 0 AND Headcount <= 100),

	Intensity NUMERIC CHECK(Intensity IS 'Intensity of deprivation Regional' OR
							Intensity >= 0 AND Intensity <= 100),

	FOREIGN KEY(ISO) REFERENCES MPI_national
);

.mode csv
.import MPI_national.csv MPI_national
.import MPI_subnational.csv MPI_subnational
.mode column
select Country, MPI_urban, MPI_rural from MPI_national where MPI_urban >= 0.1 and MPI_rural >= 0.2;
select Country, MPI_urban, MPI_national from MPI_subnational where MPI_national is not null;
select Country, MPI_urban, MPI_rural, MPI_national from MPI_subnational where MPI_urban >= 0.1 and MPI_rural >= 0.2 and MPI_national is not null;
-- sort countries in asecnding order