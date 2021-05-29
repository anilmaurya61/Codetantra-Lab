def frequency (seq):
	
	
	# write your code here
	d={}
	for i in seq:
		d[i]=d.get(i,0)+1
	
	min_num = min(d.values())
	max_num = max(d.values())
	
	min_list=[k for k,v in d.items() if v==min_num]
	max_list=[k for k,v in d.items() if v==max_num]
	
	return(sorted(min_list),sorted(max_list),min_num,max_num)
	
	
	
	
	
	
l1 = [int(x) for x in input("Please enter integers separated by spaces: ").split()]
print (frequency(l1))