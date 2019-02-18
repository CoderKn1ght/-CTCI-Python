class Graph(object):

    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacenct_list = [[] for x in range(number_of_vertices)]

    def add_edge(self, from_vertice, to_vertice):
        self.adjacenct_list[from_vertice].append(to_vertice)

    def get_input_edges_from_user(self):
        print("space seprated edges with comma seprated vertices of edges")
        string = input()
        tokens = string.split(' ')
        for token in tokens:
            numbers = token.split(',')
            self.add_edge(int(numbers[0]),int(numbers[1]))
        self.print_graph()

    def get_edges_of_vertex(self, vertex):
        return self.adjacenct_list[vertex]

    def print_graph(self):
        print("adjacency list is: ",self.adjacenct_list)
