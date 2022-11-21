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

    def graph_to_sat(self):
        
        # all of these have to be notted individually and then added
        sat_arr = []
        # Ensures that a node can be coloured by only one colour
        for node in self.nodes:
            sat_arr.append(["-N{}C{}".format(node.label,j) for j in range(1,4)])
            sat_arr.append(["N{}C1".format(node.label), "N{}C2".format(node.label)])
            sat_arr.append(["N{}C2".format(node.label), "N{}C3".format(node.label)])
            sat_arr.append(["N{}C1".format(node.label), "N{}C3".format(node.label)])
        
        edge_set = set()
        for node in self.nodes:
            for edge_label in node.edges:
                if frozenset({node.label,edge_label}) not in edge_set:
                    sat_arr.append(["N{}C1".format(node.label), "N{}C1".format(edge_label)])
                    sat_arr.append(["N{}C2".format(node.label), "N{}C2".format(edge_label)])
                    sat_arr.append(["N{}C3".format(node.label), "N{}C3".format(edge_label)])

                    # To prevent creating redundant boolean expressions
                    edge_set.add(frozenset({node.label,edge_label}))
        
        return sat_arr