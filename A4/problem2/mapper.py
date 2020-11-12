def mapper (key, val):
	outputList = []

	try:
		for col in val['subnational']:
			Mpi_Urban_Val = float(val['MPI Urban'])
			Mpi_Rural_Val = float(val['MPI Rural'])
			Mpi_National_Val = float(col['MPI National'])
			Country_Val = col['Country']
			tuple = (key, (Country_Val, Mpi_Urban_Val, Mpi_Rural_Val, Mpi_National_Val))
			if tuple not in outputList:
				outputList.append(tuple)

	except:
		pass

	return outputList	
