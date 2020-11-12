import math

def mapper (key, val):
	tupleList = []

	try:
		# operations for ((H, 30), (<country name>, <subnational region name>, <subnational region deprivation intensity>))
		for col in val['subnational']:
			HCR_bin = (math.trunc(float(col['Headcount Ratio Regional']))/10)*10
			tupleH1 = ('H', HCR_bin)
			tupleH2 = (col['Country'], col['Sub-national region'], float(col['Intensity of deprivation Regional']))
			tupleList.append((tupleH1, tupleH2))
		
		# operations for ((I, 20), (<country name>, <subnational region name>, <subnational region headcount ratio>))
		for col in val['subnational']:
			IDU_bin = (math.trunc(float(col['Intensity of deprivation Regional']))/10)*10
			tupleI1 = tupleH1 = ('I', IDU_bin)
			tupleI2 = (col['Country'], col['Sub-national region'], float(col['Headcount Ratio Regional']))
			tupleList.append((tupleI1, tupleI2))
			
	except:
		pass

	return tupleList