import time

class Node():
    def __init__(self,label):
        self.label = label
        self.colour = 0
        self.edges = set()
    
    def add_edge(self,dst_label):
        '''
            Input:
                dst_label: the label of a node that has an edge with the current node
            Processing:
                Adds the label to the edges set
        '''
        self.edges.add(dst_label)
    
    def get_colour(self):
        '''
            Returns the character for colour based on a predefined map
            if key is not present in map ERR is returned
        '''
        colour_map = {0:"NO", 1: "R", 2: "G", 3:"B"}
        if self.colour > 3:
            return "ERR"
        return colour_map[self.colour]

class Graph():
    def __init__(self):
        self.nodes = []
    
    def init_nodes_from_adj_matrix(self,adj_matrix):
        '''
            Input:
                adj_matrix: Adjacency matrix representation of graph
            Output:
                returns a graph object representing the graph given as input
        '''
        for i in range(len(adj_matrix)):
            node = Node(str(i+1))
            for j in range(len(adj_matrix[i])):
                if adj_matrix[i][j] != 0:
                    node.add_edge(str(j+1))
            self.nodes.append(node)
    
    def find_node_index_w_label(self,label):
        '''
            Input:
                label: The label of a node
            Output:
                returns the node index with the corresponding label
                otherwise returns None
        '''
        for i in range(len(self.nodes)):
            if self.nodes[i].label == label:
                return i
        return None
    
    def load_node_colours(self,colour_arr):
        '''
            Input:
                colour_arr: list of size (num of vertices in graph) having numbers representing colours
            Processing:
                Assigns a colour to each node in graph based on the input colour array
        '''
        for i in range(len(self.nodes)):
            self.nodes[i].colour = colour_arr[i]
    
    def print_graph_w_colours(self):
        '''
            Printing the the label of each node in a graph along with its colour
        '''
        for i in range(0,len(self.nodes)):
            print("{} : {}".format(self.nodes[i].label,self.nodes[i].get_colour()))

def is_safe_graph(graph,colour_arr,node_index):
    '''
        Input:
            graph: graph as a Graph Object
            colour_arr: list of size (num of vertices in graph) having numbers representing colours
            node_index: index of node of graph currently being processed
        
        Output:
            (true) if the current node does not share the same colour with any of its neighbours
            (false) otherwise
    '''
    neigh_set = graph.nodes[node_index].edges
    for label in neigh_set:
        if colour_arr[node_index] == colour_arr[graph.find_node_index_w_label(label)]:
            return False
    return True


def graph_colouring_backtracking(graph,colour_arr,colour_count,node_index):
    '''
        Input:
            graph: graph as a Graph Object
            colour_arr: list of size (num of vertices in graph) having numbers representing colours
            colour_count: the maximum number of colours
            node_index: index of node of graph currently being processed
        
        Output:
            (true) if graph is colourable by colour_count number of colours
            (false) otherwise
    '''

    if node_index >= len(graph.nodes):
        return True
    
    # Assigning every colour to every vertex
    for c in range(1,colour_count+1):
        colour_arr[node_index] = c
        if is_safe_graph(graph,colour_arr,node_index):

            if graph_colouring_backtracking(graph,colour_arr,colour_count,node_index+1):
                return True  

            colour_arr[node_index] = 0

    return False

if __name__ == "__main__":

    # Adjacency Matrix
    graph_adj_matrix = [[0,1,1],
                        [1,0,1],
                        [1,1,0]]
    
    # Initialize graph object
    g = Graph()
    g.init_nodes_from_adj_matrix(graph_adj_matrix)

    # Initializing colours of all vertices
    colour_arr = [0 for _ in range(len(g.nodes))]

    # Our case considers 3 colourable
    colour_count = 3

    start = time.time()
    # Running the backtracking algorithm
    isColourable = graph_colouring_backtracking(g, colour_arr=colour_arr, colour_count=colour_count, node_index=0)
    end = time.time()

    # Printing result
    if isColourable:
        print("This graph is 3-colourable. TIME TAKEN: {}".format(end-start))
        g.load_node_colours(colour_arr)
        g.print_graph_w_colours()
    else:
        print("This graph is NOT 3-colourable. TIME TAKEN: {}".format(end-start))



    

