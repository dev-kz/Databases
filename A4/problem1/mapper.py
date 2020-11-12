import math

def mapper (key, val):
	outputList = []
	
	try:
		Mpi_Urban_Val =  float(val['MPI Urban'])
		Mpi_Rural_Val =  float(val['MPI Rural'])
		Country_Val = val['Country']

		if Mpi_Urban_Val >= 0.1 and Mpi_Rural_Val >= 0.2:
			tuple = (Country_Val, Mpi_Urban_Val, Mpi_Rural_Val)

			# key is ISO
			outputList.append((key, tuple))		
	except:
		pass

	return outputList	
