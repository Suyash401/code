def min_houses(candies_list, G):

	# stores the current window sum
	total = 0

	# stores the result
	numb_houses = float('inf')

	# stores window's starting index
	left = 0

	# maintain a sliding window [left..right]
	for right in range(len(candies_list)):

		# include current element in the window
		total += candies_list[right]

		#Reducing total if it becomes more than total candies
		while total >= G and left <= right:
			# update the result if current numb_houses is less
			# than minimum found so far
			numb_houses = min(numb_houses, right - left + 1)

			# remove elements from the left side till total becomes usuable
			total -= candies_list[left]
			left = left + 1

	# return result
	return numb_houses
G = int(input("Enter total number of Candies: "))
n = int(input("Enter total number of houses: "))
candies_from_each_house = input().split()
candies_int = []
for x in candies_from_each_house:
        candies_int.append(int(x))

if len(candies_int) == n:
        length = min_houses(candies_int, G)
        if length != float('inf'):
                print("Number of houses sabin needs to carol:", length)
        else:
                print("NO")
else:
        print("Number of Houses don't match the given input")
