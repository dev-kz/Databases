def getAverage(intputList):
	mpiNationalList = []

	for val in intputList:		
		# choose MPI National value (float) from the tuple (country, MPI National)
		mpiNationalList.append(val[1])

	return sum(mpiNationalList) / len(mpiNationalList)

def reducer (key, intputList):
	return [(key, getAverage(intputList))]
