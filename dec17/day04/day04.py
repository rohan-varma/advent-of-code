if __name__ == '__main__':
	print(sum([1 if len(set(phrase)) == len(phrase) else 0 for phrase in [[s.strip() for s in line.split(" ")] for line in open('input.txt').readlines()]]))
