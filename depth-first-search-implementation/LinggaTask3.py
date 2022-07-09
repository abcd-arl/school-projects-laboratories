from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)
		
	def get_children(self, v):
		return self.graph[v]
		
	def print_graph(self):
		print("ADJACENCY LIST")
		for key in self.graph:
			print("({} -> {})".format(key, self.graph[key]))
		
	def get_included_nodes(self, v, limit, depth = 1, included = None):
		if included is None:
			included = defaultdict(list)

		included[v] = self.get_children(v)
		depth += 1
		
		if depth < limit:
			for i in included[v]:
				self.get_included_nodes(i, limit, depth, included)
	
		return included

	def DLS(self, v, target, included, found = False, visited = None):
		if visited is None:
			visited = set()
		
		visited.add(v)
		print(v, end=' -> ' )
		
		if v == target:
			return True

		for nxt in included[v]:
			if nxt not in visited and not found:
				found = self.DLS(nxt, target, included, found, visited)
				
		return found

if __name__ == "__main__":
	
	g = Graph()

	vertices = int(input("Enter the required number of vertices: "))
	edges = int(input("Enter the required number of edges: "))

	for i in range(edges):
		x1, x2 = input("Enter the format of the edges:").split() 
		g.add_edge(int(x1), int(x2))

	target = int(input("Enter the target of the depth-limited search: "))
	limit = int(input("Enter the limit level of the depth-limited search: "))
	print()

	g.print_graph()
	included = g.get_included_nodes(1, limit)
	print()
	print("DLS: ", end=" ")
	
	if g.DLS(1, target, included):
		print("The target is found within the limit.")
	else:
		print("The target is NOT found within the limit.")

