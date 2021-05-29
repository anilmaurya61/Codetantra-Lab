def r_sum(nested_num_list):

# write your code here
	total=0
	for element in nested_num_list:
		if type(element) == type([]):
			total +=r_sum(element)
		else:
			total +=element
	return total

	
L1 = [1, 10, 9, [3, 5, 7], [5, [6, 7], 97]]
print(r_sum(L1))