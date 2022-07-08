from util import initialize_graph
import sys

max_possible_value = sys.maxsize

def astar_search(graph, start, goal):

    path = []
    explored_nodes = list()

    if start == goal:
        return path, explored_nodes

    path.append(start)
    path_cost = heuristic(start, goal)
    frontier = [(path_cost, path)]
    while len(frontier) > 0:
        path_cost_till_now, path_till_now = pop_frontier(frontier)
        current_node = path_till_now[-1]
        path_cost_till_now = path_cost_till_now - heuristic(current_node, goal)
        explored_nodes.append(current_node)
        if current_node == goal:
            return path_till_now, explored_nodes

        neighbours = graph[current_node]

        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=False)
        neighbours_list_str = [str(n) for n in neighbours_list_int]

        for neighbour in neighbours_list_str:
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)
            
            extra_cost = 1
            neighbour_cost = extra_cost + path_cost_till_now + heuristic(neighbour, goal)
            new_element = (neighbour_cost, path_to_neighbour)

            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(neighbour, frontier)

            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.pop(indexx)
                    frontier.append(new_element)

    return None, None


def pop_frontier(frontier):
	if len(frontier) == 0:
		return None
	min = max_possible_value
	max_values = []
	
	for key, path in frontier:
		if key == min:
			max_values.append(path)
		elif key < min:
			min = key
			max_values.clear()
			max_values.append(path)
	
	max_values = sorted(max_values, key=lambda x: x[-1])
	desired_value = max_values[0]
	frontier.remove((min, max_values[0]))
	return min, desired_value


def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None

def heuristic(node, goal):
	x1, y1 = divmod(int(node), 8)
	x2, y2 = divmod(int(goal), 8)
	return abs(x1 - x2) + abs(y1 - y2)
