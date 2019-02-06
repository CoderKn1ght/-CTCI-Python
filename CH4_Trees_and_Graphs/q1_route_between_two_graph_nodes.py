from CH4_Trees_and_Graphs.adjacency_list_graph import Graph

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

def find_path_helper(current, target, visited):
    visited[current] = True

    for edge in graph.get_edges_of_vertex(current):
        if edge == target:
            return True
        if not visited[edge]:
            if find_path_helper(edge, target, visited):
                return True

    return False

def find_path_between_routes(vertex1, vertex2):
    visited = [False] * number_of_vertices
    return find_path_helper(vertex1, vertex2, visited)

print(find_path_between_routes(vertex1, vertex2))
print(find_path_between_routes(vertex2, vertex1))