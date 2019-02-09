nums = [9,26,24,17,4,22]

def bubblesort(lst):
	srt = True
	while srt:
		srt = False
		for i in range(len(lst)):
			if i+1 > len(lst)-1:
				break
			elif lst[i+1]<lst[i]:
				lst[i+1],lst[i] = lst[i],lst[i+1]
				srt = True
	return print(lst)

def selectsort(lst):
	for i in range(len(lst)):
		mi = lst.index(min(lst[i:]))
		lst[i],lst[mi] = lst[mi],lst[i]
	return print(lst)

selectsort(nums)
