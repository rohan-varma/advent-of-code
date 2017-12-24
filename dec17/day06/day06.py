def repeat_until_cycle(li):
	count = 0
	seen_with_count = {tuple(li): count} # tuple to count of when it was seen, initially 0
	while True:
		if count % 500 == 0:
			print('count is {}'.format(count))
		# find the max in li, breaking ties by idx
		max_idx, max_val = max(([idx, val] for idx, val in enumerate(li)), key = lambda l: l[1])
		# do a redistribution op
		li[max_idx] = 0
		num_to_distribute = max_val
		cur_idx = max_idx + 1 if max_idx + 1 < len(li) else 0
		while num_to_distribute:
			# cur_idx is going to be valid, distribute 1 here and move on
			li[cur_idx]+=1
			num_to_distribute-=1
			cur_idx = cur_idx + 1 if cur_idx + 1 < len(li) else 0
		# cool, that was one distribution
		count+=1
		# now check if we've ever see this arrangement
		if tuple(li) in seen_with_count:
			return count, count - seen_with_count[tuple(li)]
		else:
			seen_with_count[tuple(li)] = count

if __name__ == '__main__':
	dummy = [0, 2, 7, 0]
	print(repeat_until_cycle(dummy))
	nums = [int(num) for num in open('input.txt').read().split()]
	print(repeat_until_cycle(nums))
