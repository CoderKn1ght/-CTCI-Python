from CH4_Trees_and_Graphs.adjacency_list_graph import Graph
from collections import deque

number_of_vertices = 4
search_start_vertex = 1
graph = Graph(number_of_vertices)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)

graph.print_graph()


def breadth_first_Search(start_vertex):
    visited = [False] * number_of_vertices

    queue = deque()

    queue.append(start_vertex)
    visited[start_vertex] = True

    answer_list = []

    while queue:
        temp = queue.pop()
        answer_list.append(temp)

        for edge in graph.get_edges_of_vertex(temp):
            if not visited[edge]:
                queue.appendleft(edge)
                visited[edge] = True

    return answer_list

print("bfs with start vertex {0} is: {1}".format(search_start_vertex,breadth_first_Search(search_start_vertex)))