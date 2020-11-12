def mapper (key, val):
	outputList = []

	try:	
		for col in val['subnational']:
			Country_val = col['Country']
			Mpi_National_Val = float(col['MPI National'])

			# redefine the key for grouping
			key = col['World region']		
			tuple = (key, (Country_val, Mpi_National_Val))

			# avoid duplicates
			if tuple not in outputList:
				outputList.append(tuple)
			
	except:
		pass
	
	return outputList
