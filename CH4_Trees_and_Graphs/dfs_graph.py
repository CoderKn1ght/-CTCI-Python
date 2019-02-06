from CH4_Trees_and_Graphs.adjacency_list_graph import Graph

number_of_vertices = 4
search_start_vertex = 1
graph = Graph(number_of_vertices)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)

def dfs_helper(visited, current, answer_list):
    visited[current] = True
    answer_list.append(current)

    for edge in graph.get_edges_of_vertex(current):
        if not visited[edge]:
            dfs_helper(visited, edge, answer_list)

    return answer_list

def depth_first_Search(search_start_vertex):
    visited = [False] * number_of_vertices
    answer_list = []

    dfs_helper(visited, search_start_vertex, answer_list)

    return answer_list

print(depth_first_Search(search_start_vertex))