def mapper (key, val):
	outputList = []

	try:
		for col in val['subnational']:
			Country_val = col['Country']
			Mpi_Urban_Val = float(val['MPI Urban'])
			Mpi_Rural_Val = float(val['MPI Rural'])

			# redefine key
			key = col['World region']
			
			tuple = (key, (Country_val, Mpi_Urban_Val, Mpi_Rural_Val))
			
			# avoid duplicates
			if tuple not in outputList:
				outputList.append(tuple)
	except:
		pass

	return outputList
