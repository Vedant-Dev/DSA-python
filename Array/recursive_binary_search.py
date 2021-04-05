def search(list,target):
	if len(list) == 0:
		return False
	else:
		mid_point = (len(list)) // 2
	
	if list[mid_point] == target:
		return True
	else:
		if list[mid_point] < target:
			return search(list[mid_point + 1:],target)
		else:
			return search(list[:list[mid_point] - 1],target)
