import matplotlib.pyplot as plt
import networkx as nx

def convert_result_percent(result, total):
    for k in result.keys():
        result[k] = result[k]/total
    return result

def set_threshold(num_node):
    if num_node == 3:
        return 0.015
    else:
        return 0.1   

def create_graph_from_adj(adjacency_matrix):
    G = nx.Graph(adjacency_matrix, nodetype=int)
    #print(G.edges())
    edges = G.edges()
    '''
    bidir_edges = []
    for i in edges:
        if (i[1], i[0]) not in bidir_edges:
            bidir_edges.append(i)
    print(bidir_edges)
    '''
    if (len(edges) > 0):
        G.add_edges_from(edges)
        nx.draw(G, node_size=500, with_labels = True)
    else:
        G=nx.Graph()
        G.add_node("1")
        nx.draw(G, with_labels = True)
    file_path = "output/graphs/" + str(len(adjacency_matrix)) + "-nodes/" +"uncoloured.png"
    plt.savefig(file_path)
    return edges

def colour_graph(edges, colours, possibility_number, num_nodes):
    
    G = nx.Graph()
    #print(colours)
    if(len(edges) > 0):
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, scale=5)
        plt.figure()
        nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
        node_size=400, node_color=colours, alpha=0.9,
        labels={node: node for node in G.nodes()})

    else:
        G.add_node("1")
        pos = nx.spring_layout(G, scale=5)
        nx.draw(G, pos, node_size=400, node_color=colours)
    
    file_path = "output/graphs/" + str(num_nodes) + "-nodes/coloured" 
    plt.savefig(file_path + str(possibility_number) + ".png")
    return file_path

def split_possibility(result, num_qubits):
    #return [result[:3], result[3:6], result[6:]]
    i = 0
    states = []
    while (i < len(result)):
        states.append(result[i:i+num_qubits])
        i +=  num_qubits
    return states