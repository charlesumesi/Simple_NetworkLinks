# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020

@author: Charles Umesi
"""

import networkx as nx
import matplotlib.pyplot as plt

def create_network_from_links():
    
    '''Generates network graphs from input nodes'''
    
    # Network details
    a = input('Give the name for your network : ')
    b = (input('Enter the nodes for your network (separated by commas) : ')).split(',')
    c = int(input('How many links will your network have? '))
    d = "Enter one link connecting two nodes in the following manner: for example, if linking 'A' to 'B', type, 'A' LINK 'B' : "
    e = [list(input(d)) for _ in [0]*c]
    f = []
    
    # Processing of input data so that it is suitable for nx
    for i in e:
        g = (''.join(i)).replace('LINK'.upper(), ',')
        f.append(g)
    
    # Final pre-nx processing before transferring to nx for further handling
    G = nx.Graph()
    G.add_nodes_from(b)
    for i in f:
        eval("G.add_edge(" + i + ")")
    
    nx.draw(G, with_labels = True)
    
    # Generation of graph by plt
    plt.savefig(a + '.png')  # Saves an image file of the graph in the same folder as this program
    
    return plt.show()

create_network_from_links()