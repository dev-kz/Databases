def mapper (key, val):
	tupleList = []

	try:
		for col in val['subnational']:
			tuple = (col['World region'], float(col['MPI Regional']))
			tupleList.append(tuple)
	except:
		pass

	return tupleList
