
def num_jumps(li):
	count = 0
	cur_idx = 0
	while cur_idx >= 0 and cur_idx < len(li):
		if count % 1000 == 0:
			print(count)
		# we're not outside the list
		count+=1
		# make a jump by li[cur_idx] and increment li[cur_idx] by -1 if we jumped more than 3 else 1 (part 2)
		jump_amount = li[cur_idx]
		li[cur_idx]+= -1 if jump_amount >= 3 else 1
		cur_idx+=jump_amount
	return count

if __name__ == '__main__':
	lines = [int(line.strip()) for line in open('input.txt').readlines()]
	print(num_jumps(lines))
