
def compare_and_exchange(list0):
	if len(list0)<=1:
		return list0
	elif len(list0)==2:
		if list0[0]>list0[1]:
			new_list = [list0[1], list0[0]]
			return new_list
		else:
			return list0
	else:
		raise("Error compare")

def merge_two_parts(part1, part2):
	new_list = []
	n_part1 = len(part1)
	n_part2 = len(part2)
	i = 0
	j = 0

	while(i<n_part1 and j<n_part2):
		val1 = part1[i]
		val2 = part2[j]
		if val1>val2:
			new_list.append(val2)
			j+=1
		else:
			new_list.append(val1)
			i+=1

	if i<n_part1:
		new_list += part1[i:]
	elif j<n_part2:
		new_list += part2[j:]

	return new_list


def seperate_and_merge(list0):
	if len(list0)<=2:
		return compare_and_exchange(list0)

	i_sep = len(list0)//2
	part1 = list0[:i_sep]
	part2 = list0[i_sep:]

	part1 = seperate_and_merge(part1)
	part2 = seperate_and_merge(part2)
	sorted_list = merge_two_parts(part1, part2)
	return sorted_list



def main():
	list0 = [2,2,36,9,10,236,2,8,25,1000]
	sorted_list = seperate_and_merge(list0)

	print("list0:      ", list0)
	print("sorted_list:", sorted_list)



if __name__ == "__main__":
	main()
	print("\nDone!\n")