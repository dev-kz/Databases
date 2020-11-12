def Average(list): 
    return sum(list) / len(list) 

def reducer (key, list_of_vals):
	avg_list_vals = Average(list_of_vals)
	return [(key, avg_list_vals)]

