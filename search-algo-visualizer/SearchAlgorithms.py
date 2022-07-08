"""
*****************************************
Laboratory Exercise 1 - Search Algorithms
2019-9183 Abdulrahamn Lingga - ITE153 IT3B
*****************************************
"""

from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class SearchAlgorithms:
	"""Discover and visualize paths of the initial graph using different kinds of search algorithm.
	
	This class visualizes the graph and its paths from the initial state to the goal state using Breadth-First Search,
	Depth-First Search, and A* Search algorithms. Please keep in mind that the search algorithms takes alphabetical ordering
	upon choosing where to traverse first (e.g., among nodes A, B, and F, node A is selected.) The paths are also shown simultaneously
	in the plot where
	
		RED edges indicate the BFS path,
		BLUE edges indicate the DFS path, and
		YELLOW edges indicate the A* path.
			
	Having different initial state and goal state than the default values from each search may cause the colored edges to overlap.
	It is chosen to show the paths simultaneously as they all traverse in different paths using the default values of initial
	node and goal node. Please see visualize_graph function for more details.
		
	"""
	
	def __init__(self):
		self.graph = defaultdict(list,
					{	'S': [('A', 2), ('B', 1), ('F', 3)],
						'B': [('D', 2), ('E', 4),],
						'A': [('C', 2), ('D', 3)],
						'F': [('G', 6)],
						'C': [('G', 4)],
						'D': [('G', 4)]
					})
					
		self.heuristics = {	'S': 6,
							'A': 4,
							'B': 5,
							'C': 2,
							'D': 2,
							'E': 8,
							'F': 4,
							'G': 0	}
	
	def bfs(self, start='S', target='G'):
		""""Breadth-First Search
		
		Return a list of ordered nodes as final path of the breadth-first search.
		
		Parameters
		----------
		start (key, optional) : The starting state towards the goal state.
				
		target (value, optional) : The goal state.
		
		"""
		
		queue = []
		queue.append([start])
		
		while queue:
			path = queue.pop(0)
			node = path[-1]
			
			if node == target:
				return path
			
			for nxt, weight in self.graph[node]:
				new_path = list(path)
				new_path.append(nxt)
				queue.append(new_path)
					
		return False

	def dfs(self, start='S', target='G', path=[]):
		""""Depth-First Search
		
		Return a list of ordered nodes as final path of the depth-first search.
		
		Parameters
		----------
		start (key, optional) : The starting state towards the goal state.
				
		target (value, optional) : The goal state.
				
		path (list, optional) : A list to have nodes that are orderly visited until the goal state or None.
		
		"""
		
		path = path + [start]
		if start == target:
			return path
			
		for node, weight in self.graph[start]:
			if node not in path:
				newpath = self.dfs(node, target, path)
				if newpath: 
					return newpath
		return None
		
	def a_star(self, start='S', target='G'):
		""""A* Search
		
		Return a list of ordered nodes as final path of the A* search.
		
		Parameters
		----------
		start (key, optional) : The starting state towards the goal state.
				
		target (value, optional) : The goal state.
		
		"""
		
		visited = set()
		q = []
		heapq.heappush(q, (6, start, 0, []))
		
		while q:
			current = heapq.heappop(q)
			
			if current[1] == target:
				break
			
			for nxt, w in self.graph[current[1]]:
				if nxt not in visited:
					heapq.heappush(q, (
								w + current[2] + self.heuristics[nxt],
								nxt,
								w + current[2],
								current[3] + [current[1]]
								))
		
		return current[3] + [current[1]]
	
					
	def visualize_graph(self):
		""""Show the visualization.
		
		Visualize the graph and its paths from using breadth-first, depth-first, 
		and a* search algorithms.
				
		Note
		----
		The paths are simultaneously shown and having different initial state and goal state than the default values from each search
		may cause the colored edges to overlap. If you wish to change the states in default parameters and avoid to overlap paths, you may
		separate the display by omitting the for loop and using the following code instead:
			
			>>> p = [(path[n],path[n+1]) for n in range(len(path)-1)] # where path is a list returned from one of the searches
			>>> nx.draw_networkx_edges(G, pos=pos, edgelist=p, edge_color='r')
		
		"""
		
		G = nx.DiGraph()
		G.add_weighted_edges_from([(parent, child, weight) for parent, children in self.graph.items()
												  for child, weight in children])
		pos = {	'S': (-1, -0.25),
				'A': (-0.7, -0.25),
				'B': (-0.7, -0.35),
				'F': (-0.55, -0.15),
				'C': (-0.4, -0.25),
				'D': (-0.4, -0.3),
				'E': (-0.4, -0.4),
				'G': (-0.1, -0.25)
				}
		
		nx.draw_networkx(G,pos)
		labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
		
		paths = [self.bfs(), self.dfs(), self.a_star()]
		colors = ['r', 'b', 'y']
		
		for i, path in enumerate(paths):
			p = [(path[n],path[n+1]) for n in range(len(path)-1)]
			nx.draw_networkx_edges(G, pos=pos, edgelist=p, edge_color=colors[i])
			
		plt.show()

if __name__ == "__main__":
	
	g = SearchAlgorithms()
	g.visualize_graph()
	
