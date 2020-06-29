# Simple_NetworkLinks
A Python code that constructs network graphs with simple links (that is, unweighted links)
```python
import networkx as nx
import matplotlib.pyplot as plt

def create_network_from_links():
    
    '''Generates network graphs from input nodes'''
    
    # Network details
    a = input('Give the name for your network : ')
    b = (input('Enter the nodes for your network (separated by commas) : ')).split(',')
    c = int(input('How many links will your network have? '))
    ...
```
