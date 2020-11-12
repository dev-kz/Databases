import math

def mapper (key, val):

	tupleList = []
	try:
		# operations for ((H, 30), (<country name>, <urban deprivation intensity>))
		HCRU_bin = (math.trunc(float(val['Headcount Ratio Urban']))/10)*10
		tupleH1 = ('H', HCRU_bin)
		tupleH2 = (val['Country'], float(val['Intensity of Deprivation Urban']))
		tupleList.append((tupleH1, tupleH2))
	
		# operations for ((I, 20), (<country name>, <urban headcount ratio>))
		IDU_bin = (math.trunc(float(val['Intensity of Deprivation Urban']))/10)*10
		tupleI1 = ('I', IDU_bin)
		tupleI2 = (val['Country'], float(val['Headcount Ratio Urban']))
		tupleList.append((tupleI1, tupleI2))
			
	except:
		pass
	
	return tupleList
