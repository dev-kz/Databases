def getAvgUrban(intputList):
	mpiUrbanList = []
	for col in intputList:		
		# choose MPI Urban value and place it in a new set
		mpiUrbanList.append(col[1])

	return sum(mpiUrbanList) / len(mpiUrbanList)

def getAvgRural(intputList):
	mpiRuralList = []
	for col in intputList:		
		# choose MPI Rural value and place it in a new set
		mpiRuralList.append(col[2])

	return sum(mpiRuralList) / len(mpiRuralList)

def reducer (key, intputList):
	return [(key, (getAvgUrban(intputList), getAvgRural(intputList)))]