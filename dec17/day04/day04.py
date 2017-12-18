def count_anagrams(phrase):
	sorted_to_occ = {}
	for x_ in phrase:
		x = "".join(sorted(x_))
		if x in sorted_to_occ:
			sorted_to_occ[x]+=1
		else:
			sorted_to_occ[x]=0
	return sum(sorted_to_occ.values())

def is_valid(phrase):
	return count_anagrams(phrase) == 0

if __name__ == '__main__':
	print(sum([1 if is_valid(phrase) else 0 for phrase in [[s.strip() for s in line.split(" ")] for line in open('input.txt').readlines()]]))
