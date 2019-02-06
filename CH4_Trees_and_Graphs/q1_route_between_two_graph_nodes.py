from CH4_Trees_and_Graphs.adjacency_list_graph import Graph
from collections import deque

number_of_vertices = 4
vertex1 = 3
vertex2 = 1

graph = Graph(number_of_vertices)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)

graph.print_graph()

def dfs_helper(current, target, visited):
    visited[current] = True

    for edge in graph.get_edges_of_vertex(current):
        if edge == target:
            return True
        if not visited[edge]:
            if dfs_helper(edge, target, visited):
                return True

    return False

def find_path_between_routes_using_dfs(vertex1, vertex2):
    visited = [False] * number_of_vertices
    return dfs_helper(vertex1, vertex2, visited)

def find_path_between_routes_using_bfs(source, target):
    visited = [False] * number_of_vertices

    queue = deque()

    queue.append(source)
    visited[source] = True

    while queue:
        temp = queue.pop()

        for edge in graph.get_edges_of_vertex(temp):
            if edge == target:
                return True
            if not visited[edge]:
                queue.appendleft(edge)
                visited[edge] = True

    return False

# print(find_path_between_routes_using_dfs(vertex1, vertex2))
# print(find_path_between_routes_using_dfs(vertex2, vertex1))

print(find_path_between_routes_using_bfs(vertex1, vertex2))
print(find_path_between_routes_using_bfs(vertex2, vertex1))