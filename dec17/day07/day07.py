class Node:
	def __init__(self, data):
		split = data.split()
		self.name = split[0]
		# hack
		try:
			self.weight = int(split[1][1:3])
		except ValueError:
			self.weight = int(split[1][1:2])

	def __str__(self):
		return 'name: {}, weight: {}'.format(self.name, self.weight)

def get_node_by_name(nodes, name):
	return [node for node in nodes if node.name == name][0]
	
if __name__ == '__main__':
	lines = [line.strip() for line in open('input.txt').readlines()]
	nodes = []
	edge_dict = {} # just going to store the names
	for line in lines:
		info = line.split('->')
		parent_node = Node(info[0])
		nodes.append(parent_node)
		if len(info) > 1:
			outgoing_edges = info[1]
			edge_dict[parent_node] = [n.strip() for n in outgoing_edges.split(",")]
	# build up the graph
	graph = {n: [] for n in nodes}
	for k, v in edge_dict.items():
		outgoing_edges = [get_node_by_name(nodes, name) for name in v]
		# if the list isn't already empty, it means we already have some edges found
		assert k in graph and not graph[k]
		graph[k] = outgoing_edges
	# now just find a node with no incoming edges
	node_to_edge_count = {n: 0 for n in nodes}
	for _, v in graph.items():
		for node in v:
			node_to_edge_count[node]+=1
	zero_incoming_edges = [node for node, edge_count in node_to_edge_count.items() if edge_count == 0]
	assert len(zero_incoming_edges) == 1
	print(zero_incoming_edges[0].name)

