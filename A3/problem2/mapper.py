import math

# function parameters:
# key: str, is the country code
# val: dict, dictionary of information about the country
def mapper (key, val):
	tupleList = []
	try:
		for col in val['subnational']:	
			if col['MPI National'] is not None: 
				# cast str to float value
				colFloat = float(col['MPI National'])

				# perform truncation
				truncated_MPI_National = (math.trunc(colFloat * 10.0))/10.0

				# insert tuple if it doesn't originally exist
				tuple = (truncated_MPI_National, col['ISO country code'])
				if tuple not in tupleList:
					tupleList.append(tuple)

			# handles unknown MPI National values and adds frequencies:
			else:
				tupleList.append((-1, col['ISO country code']))

	except:
		# handles unknown MPI National values
		tupleList.append((-1, -1))
		pass

	return tupleList	

