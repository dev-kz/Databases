def reducer (key, list_of_vals):
	maximum_val = max(list_of_vals, key = lambda item:item[2])
	return [(key, maximum_val)]

# citation: https://stackoverflow.com/questions/13145368/find-the-maximum-value-in-a-list-of-tuples-in-python