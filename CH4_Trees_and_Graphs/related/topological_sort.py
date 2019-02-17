from CH4_Trees_and_Graphs.adjacency_list_graph import Graph

def topological_sort(graph):
    graph.print_graph()
    visited = [False for i in range(6)]

    stack = []

    for i in range(6):
        if not visited[i]:
            topological_sort_util(graph, i, stack, visited)

    while stack:
        print(stack.pop())

def topological_sort_util(graph, current_vertex, stack, visited):
    visited[current_vertex] = True
    neighbours = graph.get_edges_of_vertex(current_vertex)

    for neighbour in neighbours:
        if not visited[neighbour]:
            topological_sort_util(graph, neighbour, stack, visited)

    stack.append(current_vertex)
    return stack

graph = Graph(6)
graph.add_edge(2,3)
graph.add_edge(3,1)
graph.add_edge(4,0)
graph.add_edge(4,1)
graph.add_edge(5,0)
graph.add_edge(5,1)

topological_sort(graph)