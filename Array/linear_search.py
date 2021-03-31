def linear_search(list, target):
	for item_count in range(0,len(list)):
		if list[item_count] == target:
			return item_count
	return -1
