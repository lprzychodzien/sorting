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

bubblesort(nums)
