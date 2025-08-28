import pygraphviz as pgv
import networkx as nx

from processor.processor import Processor

G = pgv.AGraph(directed=True)

p = Processor()
p.run()
print(p.get_edges())
for e in p.get_edges():
    G.add_edge(e[0], e[1])
    edge = G.get_edge(e[0], e[1])
    edge.attr['label'] = e[2]
    edge.attr['fontname'] = 'Didot'
for node in G.nodes(): node.attr['fontname'] = 'Didot'

G.layout(prog='dot')
G.draw('graph.png')
#lp = nx.dag_longest_path(nx.DiGraph(G))
#print(str(lp))
